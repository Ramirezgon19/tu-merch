# Directiva: incorporar información nueva del cliente

**Objetivo.** Que todo lo que el cliente entregue durante la ejecución —un documento, un correo, una respuesta en el grupo de WhatsApp, una corrección a algo ya enviado— se analice, se ubique y se clasifique por relevancia antes de que alguien lo use. Información que no pasó por aquí no es fuente.

**Entradas.** El material nuevo, tal cual llegó, con su fecha y quién lo envió.

## Pasos

**1. Resguardar sin exponer.** Guarda el original y su transcripción en `.tmp/fuentes/<AAAA-MM-DD>-<remitente>-<tema>/`. **Nada de esto se sube al repositorio** mientras sea público (prohibición 13) ni hasta que ADR-003 decida dónde viven las fuentes. Un mensaje de WhatsApp se trata igual que un archivo: se copia el texto literal, con fecha, hora y persona.

**2. Analizar el contenido.** Lee completo y escribe en `.tmp/fuentes/<…>/analisis.md`:
- **Qué es:** documento nuevo, versión de uno existente, respuesta a una pregunta abierta, insumo de datos o instrucción operativa.
- **Qué temas toca:** cada afirmación concreta, en una lista, con la cita literal.
- **Qué datos personales o fiscales contiene**, para tratarlos antes de cualquier uso.

**3. Ubicar cada afirmación contra lo que ya está escrito.** Para cada punto de la lista, busca dónde vive hoy ese tema —roadmap, ADR, base, directivas, issues— y anota la ruta exacta. Esto dice **dónde se organiza**: la información nueva no crea archivos nuevos si ya existe un lugar para ella.

**4. Clasificar la relevancia** de cada afirmación en una de cinco salidas, con su efecto:

| Salida | Cuándo | Qué se hace |
|---|---|---|
| **Cierra un pendiente** | Responde un `dec-NN`, un `dep-NN` o un `P0`/`P1`/`P2` | Se actualiza el issue y el ADR o la base que lo citan; el pendiente se cierra con fecha y persona |
| **Complementa** | Aporta detalle que el roadmap no cubre y no lo contradice | Se incorpora a la directiva o al documento de detalle donde vive ese tema |
| **Contradice** | Choca con el roadmap, un ADR o la base | No se aplica. ADR con `registrar_decision.md`, aunque lo nuevo parezca mejor |
| **Amplía el alcance** | Pide algo que el roadmap no incluye o que excluyó expresamente | Solicitud de cambio con impacto en alcance, precio, fechas y aceptación. **No entra al código** hasta que se apruebe |
| **Es un insumo** | Datos para el sistema: calculadora, plantillas, tablas, cotizaciones reales, conversaciones | Se anonimiza; el original queda donde ADR-003 indique |

Una sola fuente suele producir varias salidas a la vez. Clasifica afirmación por afirmación, no el documento entero.

**5. Ponderar la autoridad.** Si la fuente la firma quien decide ese tema según el roadmap (Brayan en reglas comerciales, contabilidad en lo fiscal, Miguel en lo técnico), tiene peso de decisión. Si la envía otra persona, es una propuesta que hay que confirmar con quien decide. Anótalo en el análisis.

**6. Dejar rastro.** Para cada salida, el issue o el ADR correspondiente cita la fuente **por fecha, remitente y tipo**, sin copiar contenido confidencial al repositorio. Si la base cambia, entrada en su historial con versión nueva. Si algo resultó sorpresivo —un supuesto que era falso, una regla que nadie había mencionado—, aprendizaje en `CLAUDE.md` replicado con `python3 execution/verificar_directivas.py --arreglar`.

**Salidas.** `.tmp/fuentes/<…>/analisis.md` con la ubicación y relevancia de cada afirmación; los issues, ADR o solicitudes de cambio que correspondan; un resumen en el issue que motivó la consulta o en el grupo.

## Casos extremos

- **El cliente corrige un documento sin avisar.** Compara contra la versión anterior que tengas y trata solo las diferencias con este mismo procedimiento.
- **Dos personas del cliente dicen cosas distintas.** Ninguna se aplica: se escala a quien decide ese tema y se registra.
- **La información llega por un canal informal y es crítica** (un número, un umbral, una fecha). Se pide confirmación por escrito antes de que cierre un pendiente.
- **No sabes en qué salida cae.** Ponla en «contradice» y escala: es más barato revisar una decisión que deshacer código.
