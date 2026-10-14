#!/usr/bin/env python3
"""Sondea en solo lectura qué exponen las APIs de Shopify y Mercately, sin imprimir datos.

Uso:
  python3 execution/sondear_apis.py shopify
  python3 execution/sondear_apis.py mercately [--ruta /otra/ruta?con=params ...]

Para qué sirve: saber qué campos, permisos y metacampos expone cada API antes de
diseñar los adaptadores. Imprime la FORMA de cada respuesta (claves, tipos y
tamaño de las listas), nunca los valores, para que ningún dato personal o
comercial termine en la terminal, en el historial de un agente ni en un commit.
Las únicas excepciones son datos de esquema: los permisos del token de Shopify,
el conteo de productos y la definición (namespace.key: tipo) de los metacampos.

Reglas que el script hace cumplir (guía v2 §0 y prohibiciones 1 y 7 de CLAUDE.md):
- Shopify: solo GET y consultas GraphQL sin `mutation`. El POST a
  /admin/oauth/access_token es la obtención del token (client credentials), no
  una escritura en la tienda.
- Mercately: solo GET. Las rutas por defecto se limitan al contacto QA de
  MERCATELY_QA_TELEFONO; el teléfono nunca se imprime.

Variables (desde el entorno o desde un `.env` en la raíz del repositorio, que
está en .gitignore):
  SHOPIFY_STORE            p. ej. tienda.myshopify.com
  SHOPIFY_CLIENT_ID
  SHOPIFY_CLIENT_SECRET
  SHOPIFY_API_VERSION      por defecto 2026-10 (guía v2 §2)
  MERCATELY_API_KEY
  MERCATELY_API_BASE       por defecto https://app.mercately.com/retailers/api/v1
                           (verificar contra la documentación de Mercately)
  MERCATELY_QA_TELEFONO    teléfono de un contacto QA etiquetado `prueba-luuplab`

Solo usa la biblioteca estándar, para correr igual en el Mac y en el VPS.
"""
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAUSA_SHOPIFY = 0.6  # la guía v2 §2 fija 2 solicitudes/s en REST


def cargar_env():
    ruta = os.path.join(RAIZ, ".env")
    if not os.path.exists(ruta):
        return
    for linea in open(ruta, encoding="utf-8"):
        linea = linea.strip()
        if not linea or linea.startswith("#") or "=" not in linea:
            continue
        clave, valor = linea.split("=", 1)
        os.environ.setdefault(clave.strip(), valor.strip().strip('"').strip("'"))


def requerir(*nombres):
    faltan = [n for n in nombres if not os.environ.get(n)]
    if faltan:
        raise SystemExit(f"Faltan variables: {', '.join(faltan)}. Ponlas en .env (no se sube al repositorio).")
    return [os.environ[n] for n in nombres]


def forma(valor, profundidad=0):
    """Describe la estructura de un JSON sin revelar sus valores."""
    if profundidad > 8:
        return "…"
    if isinstance(valor, dict):
        return {k: forma(v, profundidad + 1) for k, v in valor.items()}
    if isinstance(valor, list):
        if not valor:
            return "lista vacía"
        return {f"lista de {len(valor)}": forma(valor[0], profundidad + 1)}
    if valor is None:
        return "null"
    return type(valor).__name__


def pedir(metodo, url, cabeceras, cuerpo=None):
    datos = cuerpo.encode("utf-8") if isinstance(cuerpo, str) else cuerpo
    req = urllib.request.Request(url, data=datos, method=metodo, headers=cabeceras)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            texto = r.read().decode("utf-8")
            return r.status, (json.loads(texto) if texto.strip() else None)
    except urllib.error.HTTPError as e:
        cuerpo_error = e.read().decode("utf-8", "replace")[:300]
        return e.code, {"error_http": cuerpo_error}


def imprimir(titulo, estado, cuerpo):
    print(f"\n== {titulo} → HTTP {estado}")
    if isinstance(cuerpo, dict) and "error_http" in cuerpo:
        # El cuerpo de un error no trae datos de clientes; se muestra para diagnosticar.
        print(cuerpo["error_http"])
        return
    print(json.dumps(forma(cuerpo), ensure_ascii=False, indent=2))


# ---------------------------------------------------------------- Shopify

CONSULTA_SHOPIFY = """
{
  shop { name currencyCode ianaTimezone }
  productsCount(query: "status:active") { count }
  products(first: 2, query: "status:active") {
    edges { node {
      id title status vendor productType tags
      metafields(first: 20) { edges { node { namespace key type } } }
      variants(first: 3) { edges { node {
        id sku price inventoryPolicy inventoryQuantity
        metafields(first: 20) { edges { node { namespace key type } } }
      } } }
    } }
  }
}
"""


def metacampos(nodo, encontrados):
    if isinstance(nodo, dict):
        if {"namespace", "key", "type"} <= set(nodo):
            encontrados.add(f"{nodo['namespace']}.{nodo['key']}: {nodo['type']}")
        for v in nodo.values():
            metacampos(v, encontrados)
    elif isinstance(nodo, list):
        for v in nodo:
            metacampos(v, encontrados)


def sondear_shopify():
    tienda, cid, secreto = requerir("SHOPIFY_STORE", "SHOPIFY_CLIENT_ID", "SHOPIFY_CLIENT_SECRET")
    version = os.environ.get("SHOPIFY_API_VERSION", "2026-10")
    base = f"https://{tienda}"

    cuerpo = urllib.parse.urlencode({"grant_type": "client_credentials", "client_id": cid, "client_secret": secreto})
    estado, token = pedir("POST", f"{base}/admin/oauth/access_token",
                          {"Content-Type": "application/x-www-form-urlencoded"}, cuerpo)
    if estado != 200 or not token or "access_token" not in token:
        imprimir("Token (client credentials)", estado, token)
        raise SystemExit("No se obtuvo el token. Revisa SHOPIFY_STORE y las credenciales de la app.")
    print(f"== Token obtenido; expira en {token.get('expires_in', '¿?')} s. Alcances declarados: {token.get('scope', '¿?')}")
    cab = {"X-Shopify-Access-Token": token["access_token"], "Content-Type": "application/json"}

    time.sleep(PAUSA_SHOPIFY)
    estado, alcances = pedir("GET", f"{base}/admin/oauth/access_scopes.json", cab)
    print(f"\n== Permisos efectivos del token → HTTP {estado}")
    if estado == 200 and alcances:
        handles = sorted(a.get("handle", "?") for a in alcances.get("access_scopes", []))
        print(", ".join(handles) or "ninguno")
        escritura = [h for h in handles if h.startswith("write_")]
        if escritura:
            print(f"ALERTA: el token tiene permisos de escritura ({', '.join(escritura)}). Avisar a Miguel; el proyecto es solo lectura.")
    else:
        imprimir("Permisos", estado, alcances)

    if "mutation" in CONSULTA_SHOPIFY.lower():
        raise SystemExit("La consulta contiene una mutación; este script es solo lectura.")
    time.sleep(PAUSA_SHOPIFY)
    estado, datos = pedir("POST", f"{base}/admin/api/{version}/graphql.json", cab,
                          json.dumps({"query": CONSULTA_SHOPIFY}))
    imprimir(f"GraphQL Admin {version}: tienda, conteo y 2 productos de muestra", estado, datos)
    if estado == 200 and isinstance(datos, dict):
        conteo = (((datos.get("data") or {}).get("productsCount")) or {}).get("count")
        if conteo is not None:
            print(f"\nProductos ACTIVE: {conteo}")
        defs = set()
        metacampos(datos.get("data"), defs)
        print("Metacampos vistos en la muestra:", ", ".join(sorted(defs)) or "ninguno")
        if not any(d.startswith("custom.cantidad_minima") for d in defs):
            print("Nota: `custom.cantidad_minima` no apareció en la muestra; no prueba que no exista en otras variantes.")
        if datos.get("errors"):
            print("Errores GraphQL:", json.dumps(datos["errors"], ensure_ascii=False)[:500])


# ---------------------------------------------------------------- Mercately

def sondear_mercately(rutas_extra):
    (clave,) = requerir("MERCATELY_API_KEY")
    base = os.environ.get("MERCATELY_API_BASE", "https://app.mercately.com/retailers/api/v1").rstrip("/")
    cab = {"api-key": clave, "Content-Type": "application/json"}

    rutas = []
    tel = os.environ.get("MERCATELY_QA_TELEFONO")
    if tel:
        t = urllib.parse.quote(tel)
        rutas += [("Contacto QA", f"/customers/{t}"),
                  ("Conversación del contacto QA (5 mensajes)", f"/customers/{t}/whatsapp_conversations?page=1&results_per_page=5")]
    else:
        print("Sin MERCATELY_QA_TELEFONO: se omiten las rutas del contacto QA.")
    rutas += [(f"Ruta adicional {r.split('?')[0]}", r) for r in rutas_extra]
    if not rutas:
        raise SystemExit("No hay rutas que sondear. Define MERCATELY_QA_TELEFONO o pasa --ruta.")

    for titulo, ruta in rutas:
        if not ruta.startswith("/"):
            ruta = "/" + ruta
        estado, datos = pedir("GET", base + ruta, cab)
        imprimir(titulo, estado, datos)
        time.sleep(0.5)


def main():
    cargar_env()
    if len(sys.argv) < 2 or sys.argv[1] not in ("shopify", "mercately"):
        print(__doc__)
        return 2
    if sys.argv[1] == "shopify":
        sondear_shopify()
    else:
        extra = [sys.argv[i + 1] for i, a in enumerate(sys.argv) if a == "--ruta" and i + 1 < len(sys.argv)]
        sondear_mercately(extra)
    return 0


if __name__ == "__main__":
    sys.exit(main())
