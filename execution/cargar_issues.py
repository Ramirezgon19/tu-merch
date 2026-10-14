#!/usr/bin/env python3
"""Crea etiquetas, hitos e issues en GitHub desde un JSON, por la API REST, sin duplicar.

Uso:  python3 execution/cargar_issues.py <owner/repo> <archivo.json> [--en-seco]

Usa `gh api` (REST), que funciona tanto en local como en sesiones de Claude en la
nube donde GraphQL está bloqueado. Idempotente: no duplica etiquetas ni hitos, y
omite issues cuyo título ya exista, abierto o cerrado.

Formato del JSON:
{
  "labels":     {"nombre": {"color": "hex", "description": "..."}},
  "milestones": {"clave": {"title": "...", "due_on": "YYYY-MM-DD", "description": "..."}},
  "issues":     [{"title": "...", "labels": [...], "milestone": "clave", "body": "..."}]
}
"""
import json, subprocess, sys

def gh(*args, datos=None):
    cmd = ["gh", "api", *args]
    if datos is not None:
        cmd += ["--input", "-"]
        r = subprocess.run(cmd, input=json.dumps(datos), capture_output=True, text=True)
    else:
        r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"gh api {' '.join(args)}\n{r.stderr.strip()}")
    return json.loads(r.stdout) if r.stdout.strip() else None

def paginar(ruta):
    out, pagina = [], 1
    while True:
        lote = gh(f"{ruta}{'&' if '?' in ruta else '?'}per_page=100&page={pagina}")
        if not lote: break
        out += lote
        if len(lote) < 100: break
        pagina += 1
    return out

def main():
    if len(sys.argv) < 3:
        print(__doc__); return 2
    repo, archivo = sys.argv[1], sys.argv[2]
    seco = "--en-seco" in sys.argv
    d = json.load(open(archivo, encoding="utf-8"))
    pref = "[en seco] " if seco else ""

    print("== Etiquetas")
    existentes = {l["name"] for l in paginar(f"repos/{repo}/labels")}
    for nombre, v in d.get("labels", {}).items():
        if nombre in existentes:
            print(f"   existe: {nombre}"); continue
        print(f"   {pref}crear: {nombre}")
        if not seco:
            gh(f"repos/{repo}/labels", "--method", "POST",
               datos={"name": nombre, "color": v["color"], "description": v.get("description", "")})

    print("== Hitos")
    hitos = {m["title"]: m["number"] for m in paginar(f"repos/{repo}/milestones?state=all")}
    num_hito = {}
    for clave, v in d.get("milestones", {}).items():
        if v["title"] in hitos:
            num_hito[clave] = hitos[v["title"]]; print(f"   existe: {v['title']}"); continue
        print(f"   {pref}crear: {v['title']} ({v.get('due_on','sin fecha')})")
        if not seco:
            r = gh(f"repos/{repo}/milestones", "--method", "POST",
                   datos={"title": v["title"], "due_on": f"{v['due_on']}T23:59:59Z" if v.get("due_on") else None,
                          "description": v.get("description", "")})
            num_hito[clave] = r["number"]

    print("== Issues")
    titulos = {i["title"] for i in paginar(f"repos/{repo}/issues?state=all") if "pull_request" not in i}
    creados = 0
    for it in d.get("issues", []):
        if it["title"] in titulos:
            print(f"   existe: {it['title'][:80]}"); continue
        print(f"   {pref}crear: {it['title'][:80]}")
        if not seco:
            datos = {"title": it["title"], "body": it["body"], "labels": it.get("labels", [])}
            if it.get("milestone") in num_hito:
                datos["milestone"] = num_hito[it["milestone"]]
            r = gh(f"repos/{repo}/issues", "--method", "POST", datos=datos)
            print(f"      → #{r['number']}")
            creados += 1
    print(f"Listo. {creados} issues creados.")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except RuntimeError as e:
        print(f"ERROR: {e}", file=sys.stderr); sys.exit(1)
