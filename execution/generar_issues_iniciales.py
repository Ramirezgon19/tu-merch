#!/usr/bin/env python3
"""Genera .tmp/issues-iniciales.json: el primer lote de issues del cotizador.

Uso:  python3 execution/generar_issues_iniciales.py && \
      python3 execution/cargar_issues.py Ramirezgon19/tu-merch .tmp/issues-iniciales.json --en-seco

Criterio del lote: lo que se puede trabajar antes de recibir accesos del cliente
(motor, cola, esquemas, infraestructura) más las decisiones que destraban el resto.
Formato de cada issue: el de trabajo asíncrono de docs/requisitos/base-proyecto.md.
Responsable «por asignar» hasta que se repartan frentes (P1-04). Las fechas de los
hitos son las propuestas en ADR-001, no aprobadas.
"""
import json, pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SALIDA = RAIZ / ".tmp" / "issues-iniciales.json"

LABELS = {
    "D1": {"color": "1d76db", "description": "Cotizador en sombra"},
    "D2": {"color": "0e8a16", "description": "Cierre digital"},
    "D3": {"color": "5319e7", "description": "Marcación, costeo y métricas"},
    "infra": {"color": "c5def5", "description": "Despliegue, Docker, VPS (ADR-002)"},
    "tipo:setup": {"color": "ededed", "description": "Preparación del proyecto"},
    "tipo:spike": {"color": "b60205", "description": "Investigación acotada con informe"},
    "tipo:feature": {"color": "0052cc", "description": "Funcionalidad del producto"},
    "tipo:test": {"color": "006b75", "description": "Pruebas y evidencia"},
    "tipo:decision": {"color": "e4e669", "description": "Requiere un ADR o una decisión del cliente"},
    "tipo:docs": {"color": "fef2c0", "description": "Documentación"},
    "area:motor": {"color": "fbca04", "description": "motor/: precio, solicitud, estado"},
    "area:cola": {"color": "d93f0b", "description": "Cola de operaciones y modos (WF-00)"},
    "area:mercately": {"color": "bfdadc", "description": "CRM y WhatsApp"},
    "area:siigo": {"color": "f9d0c4", "description": "Registro formal y factura"},
    "bloqueado-por-cliente": {"color": "ff7619", "description": "Depende de un dep-NN o dec-NN de Tu Merch"},
}

MILESTONES = {
    "K":   {"title": "K · Arranque", "due_on": "2026-10-15", "description": "Pago inicial y accesos del hito 0. Fecha confirmada por David."},
    "D1":  {"title": "D1 · Cotizador en sombra", "due_on": "2026-10-22", "description": "Propuesto en ADR-001, pendiente de confirmación de Brayan. Evidencia A01–A09."},
    "D2":  {"title": "D2 · Cierre digital en lista de permitidos", "due_on": "2026-10-29", "description": "Propuesto en ADR-001. Hito contractual del acta de Fase 1. Evidencia A10–A12."},
    "LIVE": {"title": "Fase 1 en producción", "due_on": "2026-11-09", "description": "Propuesto en ADR-001, margen hasta el 15/11. Tras el piloto 30/10–6/11."},
    "D3":  {"title": "D3 · Marcación, costeo y métricas", "due_on": "2026-12-07", "description": "Propuesto en ADR-001. Solo si se activa la Fase 2. Evidencia M-A01–M-A07."},
}

def cuerpo(resultado, fuente, criterio, dependencia="Ninguna.", evidencia="", siguiente=""):
    partes = [
        f"## Resultado esperado\n{resultado}",
        f"## Fuente\n{fuente}",
        f"## Criterio de terminado\n{criterio}",
        f"## Dependencia\n{dependencia}",
    ]
    if evidencia: partes.append(f"## Evidencia\n{evidencia}")
    partes.append("## Responsable\nPor asignar (P1-04).")
    if siguiente: partes.append(f"## Siguiente acción\n{siguiente}")
    partes.append("_Antes de empezar: `directives/trabajar_issue.md`. Al cerrar: `directives/cierre_de_bloque.md`._")
    return "\n\n".join(partes)

I = []
def add(title, labels, milestone, **kw):
    I.append({"title": title, "labels": labels, "milestone": milestone, "body": cuerpo(**kw)})

# ---------- Decisiones que destraban ----------
add("[decision] Confirmar con Brayan el hito del 29/10 en lista de permitidos y la producción el 9/11 (ADR-001)",
    ["tipo:decision", "bloqueado-por-cliente"], "K",
    resultado="Confirmación escrita de Brayan sobre los tres puntos de ADR-001: qué entrega el hito del 29/10, que el acta y el segundo 50 % van contra ese hito, y que la producción abierta queda el 9/11.",
    fuente="`docs/decisiones/ADR-001-cronograma-y-fecha-de-salida.md`; roadmap aprobado, `GO_LIVE`.",
    criterio="ADR-001 pasa de «propuesta» a «aprobado» con fecha y cita de la confirmación. Los hitos de GitHub se ajustan si Brayan cambia algo.",
    dependencia="Brayan (Tu Merch).",
    siguiente="Alejo lo lleva al grupo de WhatsApp el 13/10 con el texto del ADR.")

add("[decision] Revisión de David de ADR-002 y acuerdo con Tu Merch sobre costo del VPS y destino final del contenedor",
    ["tipo:decision", "infra"], "K",
    resultado="ADR-002 revisado por David, y acuerdo escrito con Tu Merch sobre quién paga el VPS y dónde termina el stack al cierre.",
    fuente="`docs/decisiones/ADR-002-despliegue-en-docker-y-arquitectura-del-motor.md`; propuesta aprobada §6 (costos recurrentes a cargo de Tu Merch); anexo §4.6.",
    criterio="ADR-002 con la revisión de David registrada en su estado. Cláusula de datos y de salida del contrato de honorarios actualizadas en consecuencia.",
    dependencia="David; Brayan para el costo.",
    siguiente="David comenta el ADR en este issue; Alejo lleva el costo a Brayan.")

add("[decision] Reemitir las fechas de dep-01…dep-15 y dec-01…dec-10 con cada responsable, sobre el inicio del 15/10",
    ["tipo:decision", "bloqueado-por-cliente"], "K",
    resultado="Cada dependencia y decisión del roadmap con una fecha nueva acordada con su responsable, no desplazada automáticamente.",
    fuente="`docs/requisitos/roadmap-aprobado-20261001.md`, tablas de accesos y decisiones; base §9, advertencia de David.",
    criterio="Tabla en `docs/decisiones/ADR-001` o anexo con la fecha nueva y quién la confirmó, una fila por ID. Los issues bloqueados por cada una enlazados.",
    dependencia="Miguel, Brayan, contabilidad, comercial y operación de Tu Merch.",
    siguiente="Alejo manda la lista por el grupo el 13/10 y registra las respuestas aquí.")

add("[setup] Repartir frentes entre Alejo y David y asignar responsable único a cada issue abierto",
    ["tipo:setup"], "K",
    resultado="Cada issue abierto tiene un responsable único. Queda escrito en la base quién toma motor y esquemas, y quién toma cola, integraciones e infraestructura, o el reparto que acuerden.",
    fuente="Base §8 P1-04 y §10, «un único responsable por tarea».",
    criterio="Ningún issue abierto con responsable «por asignar». Entrada en el historial de la base.",
    dependencia="Alejo y David. Confirmar si Juanfe participa.",
    siguiente="Kickoff interno el 14/10.")

# ---------- Infraestructura (ADR-002) ----------
add("[infra] Inventario del VPS inicial y accesos SSH por persona",
    ["infra", "tipo:setup"], "K",
    resultado="Se sabe qué hay en el VPS: versión de Docker y Compose, CPU, RAM, disco, qué otras aplicaciones corren y qué puertos usan, dominio y TLS disponibles, política de respaldo. Cada miembro del equipo entra por SSH con su propia clave.",
    fuente="ADR-002; base §8 P1-05; `directives/despliegue_docker.md`.",
    criterio="`docs/operacion/vps.md` con el inventario, sin secretos ni IPs públicas si el documento va al repo del cliente. Claves SSH por persona instaladas y probadas; ninguna clave compartida.",
    dependencia="Alejo (dueño del VPS).",
    siguiente="Alejo levanta el inventario y crea los usuarios.")

add("[infra] docker-compose.yml inicial: reverse proxy con TLS, n8n, PostgreSQL y motor, aislados y portables",
    ["infra", "tipo:feature", "D1"], "D1",
    resultado="`infra/docker-compose.yml` levanta el stack completo en una máquina limpia con `docker compose up` y el `.env` de ejemplo rellenado.",
    fuente="ADR-002; `infra/README.md`; `directives/despliegue_docker.md`.",
    criterio="Red propia; solo el proxy expone 80/443; PostgreSQL y n8n sin puertos al host; volúmenes nombrados para PostgreSQL y n8n; imágenes fijadas por versión exacta verificada contra la documentación oficial; `infra/.env.example` con todas las variables. Probado en una VM o máquina limpia, con captura del `docker compose ps`.",
    dependencia="Inventario del VPS (issue anterior) para no colisionar puertos.",
    evidencia="`docs/operacion/evidencia/infra.md`: salida de `docker compose ps` y `docker volume ls` en la máquina limpia.",
    siguiente="Fijar versiones de imagen y escribir el compose.")

add("[infra] Scripts de respaldo y restauración de volúmenes, y migración simulada a una máquina limpia",
    ["infra", "tipo:feature", "D2"], "D2",
    resultado="`execution/respaldar_volumenes.sh` y `execution/restaurar_volumenes.sh` funcionan, y una migración completa origen → destino se ensayó con éxito.",
    fuente="ADR-002, reglas de portabilidad y estado; `directives/despliegue_docker.md`, procedimiento de migración.",
    criterio="Respaldo y restauración de todos los volúmenes nombrados. Migración simulada: respaldo en A, `docker compose up` en B limpia, restauración, verificación en `shadow`. Scripts para bash 3.2 o Python.",
    dependencia="`docker-compose.yml` inicial.",
    evidencia="`docs/operacion/evidencia/migracion-simulada.md` con los comandos y las salidas.",
    siguiente="Escribir los scripts junto con el compose, no después.")

# ---------- Motor, sin accesos ----------
add("[feature] Esqueleto de motor/: dominio, puertos y adaptadores en blanco, sin HTTP ni n8n en el dominio",
    ["tipo:feature", "area:motor", "D1"], "D1",
    resultado="`motor/` existe con la separación dominio / aplicación / puertos / adaptadores, y una prueba que falla si el dominio importa HTTP, n8n o un SDK de proveedor.",
    fuente="`CLAUDE.md`, arquitectura decidida; base §4 (motor separado de los adaptadores de canal).",
    criterio="Puertos declarados para Shopify (lectura), Mercately, Siigo, Bold, Drive, Telegram, con adaptadores vacíos que lanzan «no implementado». Prueba de aislamiento de imports en verde. `pytest` corre.",
    siguiente="Primer PR de código del proyecto; fija la estructura para todo lo demás.")

add("[feature] Cola de operaciones: clave única, modos off/shadow/allowlist/live y cuatro estados; prueba de que en shadow no sale nada",
    ["tipo:feature", "area:cola", "D1"], "D1",
    resultado="`motor/cola/` implementa WF-00: toda operación externa se registra como intención con clave única por destino, acción y operación; el modo decide si se ejecuta; los estados son intención, en ejecución, confirmada e incierto.",
    fuente="`directives/cola_operaciones.md`; base §5 WF-00 y §7 «Operación externa»; anexo §4.4 y §4.5. Caso A11.",
    criterio="Pruebas: en `shadow` ningún adaptador recibe llamadas; en `allowlist` solo entidades autorizadas; un evento repetido produce una sola operación; un timeout deja la operación en incierto y no la reintenta. Horario de envío aplicado con `America/Bogota`.",
    evidencia="`docs/operacion/evidencia/D1-casos.md`, sección A11.",
    siguiente="Diseñar el esquema de la tabla de operaciones antes de codificar.")

add("[feature] Instantánea versionada de cotización y bitácora de eventos: modelo y esquema",
    ["tipo:feature", "area:motor", "D1"], "D1",
    resultado="Cada cotización guarda su instantánea (precio tomado de Shopify, versión de la calculadora, disponibilidad consultada, versiones de reglas) y cada cambio de estado deja un evento con fecha, tipo, identificador y origen.",
    fuente="Paquete §14 y §15; base §7 «Cotización y revisión» y «Evento y expediente»; `CLAUDE.md` invariantes.",
    criterio="`schemas/` con el esquema de instantánea y de evento; migraciones de PostgreSQL; prueba de que una instantánea se recupera por id y de que «enviada» ≠ «leída», «ganada» ≠ «pagada» quedan como eventos distintos.",
    siguiente="Alinear con el esqueleto de `motor/`.")

add("[feature] Motor de precio: IVA, redondeo, mínimo por variante y transporte, con pruebas parametrizadas en los límites; punto de integración de la calculadora",
    ["tipo:feature", "area:motor", "D1"], "D1",
    resultado="`motor/precio/` calcula subtotal, descuento (interfaz definida, valores de desarrollo marcados sin validez comercial hasta que llegue la calculadora), IVA 19 %, mínimo por variante y transporte con umbral, de forma determinista y reproducible.",
    fuente="Paquete §09 y §10; `CLAUDE.md` reglas de negocio; casos A01, A04, A05, A07, A08.",
    criterio="Pruebas parametrizadas justo antes, en y después de cada límite; precio de Shopify nunca remarcado; marcación y transporte no elevan el tramo; COP sin decimales. La base del umbral de transporte y el redondeo quedan como parámetros con valor de desarrollo hasta `dec-01` y `dec-02`.",
    dependencia="Calculadora original (dep-06) para los tramos reales; `dec-01` y `dec-02` para redondeo y transporte. No bloquean la estructura ni las pruebas con valores de desarrollo.",
    evidencia="`docs/operacion/evidencia/D1-casos.md`, A01, A04, A05, A07, A08 parcial.",
    siguiente="Definir la interfaz de la calculadora como función pura con versión.")

add("[feature] Vigencia de cinco días hábiles con festivos de Colombia, incluidos 8/12 y 25/12, zona America/Bogota",
    ["tipo:feature", "area:motor", "D1"], "D1",
    resultado="Una función determinista calcula la fecha y hora de vencimiento de una cotización y responde si está vigente.",
    fuente="Paquete §09; caso A09; aprendizaje del 12/10 en `CLAUDE.md` sobre los festivos que faltan en el roadmap.",
    criterio="Calendario de festivos versionado en `motor/` con todos los de 2026 y 2027, incluidos los trasladados al lunes; pruebas que cruzan fin de semana, un festivo y los dos de diciembre. La hora exacta de vencimiento y si el sábado cuenta quedan parametrizados hasta `dec-03`.",
    dependencia="`dec-03` para hora y sábado; no bloquea.",
    evidencia="`docs/operacion/evidencia/D1-casos.md`, A09.",
    siguiente="Verificar la lista de festivos contra la Ley 51 de 1983 y una fuente oficial para 2027.")

add("[feature] Esquema JSON de la solicitud estructurada y su validación",
    ["tipo:feature", "area:motor", "D1"], "D1",
    resultado="`schemas/solicitud.json` define la solicitud estructurada (canal, negociación, líneas con variante y cantidad, ciudad, fecha requerida, modalidad, estado y faltantes) y `motor/solicitud/` la valida.",
    fuente="Paquete §07; base §5 WF-02 y §7 «Solicitud»; caso A06.",
    criterio="Esquema versionado; validación que marca `pendiente_datos` con la lista de faltantes en vez de rellenar con valores inventados; pruebas con solicitudes completas, incompletas y ambiguas.",
    dependencia="Las diez conversaciones anonimizadas (dep-08) para pruebas reales; no bloquea el esquema.",
    evidencia="`docs/operacion/evidencia/D1-casos.md`, A06.",
    siguiente="Diseñar el contrato JSON junto con WF-02.")

add("[test] Andamiaje de tests/ con un archivo por caso A01–A12 y M-A01–M-A07, marcados pendientes",
    ["tipo:test", "D1"], "D1",
    resultado="`tests/aceptacion/` tiene un archivo por caso con el nombre del caso, marcado como pendiente, y `pytest` los recoge.",
    fuente="Roadmap aprobado, tabla de casos; `directives/evidencia_caso.md`.",
    criterio="19 archivos, `pytest tests/aceptacion -q` muestra 19 omitidos. Cada archivo cita en su docstring qué exige el caso.",
    siguiente="Se rellenan a medida que cada feature los cubre.")

# ---------- Spike bloqueado por accesos ----------
add("[spike] Disparador de solicitudes en Mercately: listar por etapa, enganche a n8n o comando del asesor",
    ["tipo:spike", "area:mercately", "D1", "bloqueado-por-cliente"], "D1",
    resultado="Informe de una página con el resultado de las tres opciones y una recomendación, registrada como ADR.",
    fuente="Base §5 WF-01 y §6.3–6.6; anexo §2 (sin webhooks); guía v2 §1.",
    criterio="Para cada opción: viable o no, con requests y respuestas reales anonimizadas; coste en llamadas por mes contra la cuota del plan; latencia. Decisión en `docs/decisiones/ADR-003`. Máximo dos días hábiles.",
    dependencia="`dep-02` (api-key, embudo, plan y cuota) y `dep-03` (contactos de prueba). Bloqueado hasta recibirlos.",
    evidencia="`docs/operacion/evidencia/hito0-mercately.md`.",
    siguiente="Arranca el día que lleguen los accesos.")

# ---------- Docs ----------
add("[docs] Corregir los festivos del roadmap HTML (añadir 8/12 y 25/12) y regenerar la transcripción",
    ["tipo:docs"], "K",
    resultado="El roadmap original y su transcripción declaran todos los festivos de Colombia del periodo.",
    fuente="Aprendizaje del 12/10 en `CLAUDE.md`; `docs/requisitos/roadmap-aprobado-20261001.md`, sección de hitos.",
    criterio="`HOLIDAYS` del HTML incluye 2026-12-08 y 2026-12-25; la transcripción se regenera desde el HTML, no se edita a mano; la nota de «faltan» desaparece.",
    siguiente="Un PR pequeño; es el primer cambio al roadmap y conviene que David vea el procedimiento.")

SALIDA.parent.mkdir(exist_ok=True)
json.dump({"labels": LABELS, "milestones": MILESTONES, "issues": I},
          open(SALIDA, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
from collections import Counter
print(f"{len(I)} issues → {SALIDA.relative_to(RAIZ)}")
print(dict(Counter(i["milestone"] for i in I)))
