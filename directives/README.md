# directives/ — índice y mapa del roadmap a las tres capas

Las directivas son los SOP del proyecto: qué hacer, con qué entradas, con qué herramienta de `execution/`, qué sale y qué casos raros hay. El agente las lee y orquesta; no improvisa el procedimiento. Si una directiva no existe para lo que vas a hacer, pregunta antes de crearla.

| Directiva | Cuándo se usa |
|---|---|
| `trabajar_issue.md` | Antes de escribir una línea de código para un issue |
| `registrar_decision.md` | Cuando una regla o una arquitectura no está decidida |
| `evidencia_caso.md` | Al cerrar un caso de aceptación A01–A12 o M-A01–M-A07 |
| `cola_operaciones.md` | Al tocar cualquier efecto externo: WhatsApp, Siigo, Bold, Drive, Telegram, etapas del CRM |
| `despliegue_docker.md` | Al tocar `infra/`, levantar o migrar el stack |
| `cierre_de_bloque.md` | Al terminar una sesión de trabajo |
| `incorporar_fuente.md` | Cuando el cliente entrega información nueva: documento, correo o mensaje del grupo |

## El roadmap, repartido en las tres capas

El roadmap aprobado del 01/10 fija **qué** se entrega. Esta tabla dice en qué capa vive cada entregable: la directiva que lo gobierna, el código determinista que lo ejecuta y el componente del producto donde queda. Lo que no tiene directiva todavía se marca «por escribir»; se escribe cuando el issue correspondiente arranque, no antes.

### D1 · Cotizador en sombra

| Entregable del roadmap | Directiva (qué) | Ejecución (cómo, determinista) | Producto |
|---|---|---|---|
| Accesos del hito 0 probados con evidencia (dep-01 a dep-05) | `evidencia_caso.md` | por escribir: `execution/probar_acceso.py` por proveedor | `docs/operacion/evidencia/` |
| Spike del disparador en Mercately | `registrar_decision.md` | — | ADR + WF-01 |
| Solicitud estructurada con validación de esquema | por escribir: `extraer_solicitud.md` | `motor/solicitud/` con pruebas | `schemas/solicitud.json`, WF-02 |
| Motor de precio: calculadora, IVA, mínimo, transporte, vigencia | por escribir: `calcular_cotizacion.md` | `motor/precio/` con pruebas en los límites | WF-04 |
| Instantánea versionada y bitácora de eventos | `cola_operaciones.md` | `motor/estado/` | `schemas/`, PostgreSQL |
| Registro en Siigo y documento con formato | por escribir: `registrar_en_siigo.md` | adaptador Siigo detrás de puerto | WF-05 |
| Cola de operaciones con modos off/shadow/allowlist/live | `cola_operaciones.md` | `motor/cola/` con prueba de «en shadow no sale nada» | WF-00 |
| Evidencia A01–A09 | `evidencia_caso.md` | por escribir: `execution/generar_evidencia.py` | `docs/operacion/evidencia/D1-casos.md` |

### D2 · Cierre digital

| Entregable del roadmap | Directiva | Ejecución | Producto |
|---|---|---|---|
| Envío por plantilla aprobada con revisión previa | `cola_operaciones.md` | adaptador Mercately | WF-06 |
| Confirmación manual idempotente de pago; luego Bold | `cola_operaciones.md` + por escribir: `confirmar_pago.md` | `motor/pagos/` | WF-07, WF-08 |
| Cliente fiscal sin duplicados (Forms → Siigo) | por escribir: `registrar_en_siigo.md` | adaptador Siigo | WF-10 |
| Pedido al proveedor con confirmación registrada | `cola_operaciones.md` | `motor/pedidos/` | WF-09 |
| Factura borrador → aprobaciones → emisión | por escribir: `facturar.md` | adaptador Siigo | WF-10 |
| Runbook, mapeo de campos, transferencia | `cierre_de_bloque.md` | — | `docs/operacion/runbook.md` |
| Evidencia A10–A12 y regresión | `evidencia_caso.md` | `execution/generar_evidencia.py` | `docs/operacion/evidencia/D2-casos.md` |

### Infraestructura, transversal a D1 y D2

| Entregable | Directiva | Ejecución | Producto |
|---|---|---|---|
| Stack en Docker, aislado, portable (ADR-002) | `despliegue_docker.md` | `execution/respaldar_volumenes.sh`, `execution/restaurar_volumenes.sh` | `infra/docker-compose.yml` |
| Migración simulada a una máquina limpia | `despliegue_docker.md` | los mismos scripts | evidencia en `docs/operacion/` |

### D3 · Marcación, costeo y métricas

Se detalla cuando se active la Fase 2 y lleguen las tablas M01–M09 (dep-14). Reutiliza `calcular_cotizacion.md`, `cola_operaciones.md` y `evidencia_caso.md`; añade `cargar_tablas_marcacion.md` por escribir.
