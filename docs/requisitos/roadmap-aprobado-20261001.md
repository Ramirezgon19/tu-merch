# Roadmap aprobado del Cotizador · 01/10/2026

Transcripción fiel del roadmap interactivo `20261001_Roadmap_Cotizador_TuMerch.html`, que es el artefacto que Tu Merch aprobó. Se mantiene en el repositorio para que la documentación y el roadmap no puedan divergir; el HTML sigue siendo el original y esta copia se regenera cuando aquel cambie.

**Las fechas de este documento son las del roadmap aprobado, calculadas sobre un arranque el 6 de octubre que no ocurrió.** El recálculo sobre el inicio real del 15/10 está en [ADR-001](../decisiones/ADR-001-cronograma-y-fecha-de-salida.md). Ninguna fecha de aquí es compromiso vigente sin esa confirmación.

## Etapas, entregables y criterios

### K · Respuesta y arranque

**Fechas del roadmap:** 1 – 6 oct (2026-10-01 a 2026-10-06) · **Hitos del cliente:** Antes del hito 0

Cerrar el acuerdo, abrir los canales de trabajo y recibir los accesos para empezar a construir el miércoles 7 de octubre.

Momentos: Kickoff · lunes 5 de octubre · Accesos · martes 6 de octubre

**Entregables (6)**

- **NDA firmado** — Con los ajustes acordados en datos personales y cláusula penal. Firmado el 23 de septiembre.
- **Paquete de estimación de Tu merch analizado** — Definición funcional (19/09) y anexo técnico (24/09), leídos completos y cruzados con la arquitectura actual.
- **Propuesta enviada a Tu merch** — Alcance por hito, cronograma, dependencias, inversión, equipo y riesgos.
- **Reunión de cierre y kickoff** — Lunes 5 de octubre, una hora, con Brayan, Miguel y la persona comercial.
- **Grupo de trabajo en WhatsApp** — Las personas clave de Tu merch y el equipo de Luup Lab. Cada decisión queda registrada como issue el mismo día.
- **Repositorio, backlog y reglas para agentes de código** — Issues con criterio de aceptación y evidencia; CLAUDE.md y AGENTS.md en la raíz del repositorio.

**Criterios de aceptación (2)**

- **Contrato de honorarios firmado y anticipo recibido antes del miércoles 7 de octubre** — 
- **Accesos del hito 0 recibidos y probados el martes 6 de octubre** — 

### D1 · Cotizador en sombra

**Fechas del roadmap:** 7 – 14 oct (2026-10-07 a 2026-10-14) · **Hitos del cliente:** Hitos 0, 1 y 2

Desde que se dispara, una solicitud cualificada produce en menos de dos minutos una cotización correcta registrada en Siigo y un PDF con el formato de Tu merch, lista para que la persona comercial la revise y la envíe. Nada sale al cliente final de forma automática.

Momentos: Despliegue · miércoles 14 de octubre · Modo sombra

**Entregables (10)**

- **Evidencia de accesos y prueba por integración** — Shopify en lectura; Mercately crear y mover negociación; Siigo cliente, producto, cotización con URL pública y factura en pruebas; Bold en pruebas.
- **Detección de solicitudes en Mercately** — Sondeo cada 10 minutos en horario hábil, enganche al agente MIA o, como mínimo garantizado, comando del asesor con el identificador de la negociación.
- **Solicitud estructurada** — El extractor de Gemini de Tu merch, extendido con variante o color, dirección, fecha requerida y modalidad. Si algo es ambiguo, pide solo lo que falta.
- **Motor de cálculo en la plataforma de Tu merch** — Precio de Shopify, mínimo por metacampo y stock por variante, calculadora de descuentos original, IVA del 19 %, transporte a Bogotá y Sabana, vigencia de 5 días hábiles con festivos.
- **Snapshot versionado de cada cotización** — Precio tomado, versión de la calculadora y disponibilidad consultada, recuperables por identificador.
- **Cotización registrada en Siigo** — Producto creado bajo demanda con el código de la variante; cotización con enlace público; consecutivo que continúa la numeración actual.
- **PDF con el formato de Tu merch** — Generado desde la plantilla de Google Slides: portada, cuerpo con enlace a la ficha de cada producto, página institucional y términos.
- **Registro en Mercately y cola de revisión** — Enlaces de Siigo y del PDF en la negociación; alerta al asesor para aprobar o rechazar con motivo.
- **Modo sombra, alertas y repositorio** — Registra lo que haría sin efectos externos; errores al bot de Telegram; integración continua con pruebas.
- **Línea base de operación** — Volumen, tiempo manual, tasa de revisión y motivos de bloqueo, registrados desde el 6 de octubre para comparar después (§19).

**Criterios de aceptación (6)**

- **A01 a A09 con evidencia en cálculo y documento** — 
- **Las cinco cotizaciones reales de muestra reproducidas al peso** — 
- **Cero escrituras en Shopify** — 
- **Snapshot recuperable por identificador** — 
- **Ningún mensaje automático al cliente final** — 
- **Cotización y PDF listos en menos de dos minutos desde el disparo** — 

### D2 · Cierre digital

**Fechas del roadmap:** 15 – 29 oct (2026-10-15 a 2026-10-29) · **Hitos del cliente:** Hitos 3, 4 y 5

Un pedido estándar sin marcación recorre cotización, envío, pago, pedido al proveedor y factura sin volver a capturar información. La Fase 1 queda operable por Tu merch.

Momentos: Lista de permitidos · miércoles 21 de octubre · Piloto · 22 al 28 · Producción · jueves 29 de octubre

**Entregables (13)**

- **Envío de la cotización por plantilla de WhatsApp** — Con revisión del asesor antes de cada envío mientras dura la lista de permitidos. Si Meta aún no aprueba la plantilla, el asesor envía con el texto listo.
- **Confirmación de pago idempotente** — Llave Bre-B, PSE por Rappipay y transferencia, con soporte. Una confirmación repetida no crea un segundo pedido.
- **Revalidación de stock antes del cobro** — Con la regla de reserva que decida Tu merch. La cotización nunca se presenta como reserva confirmada.
- **Cliente fiscal en Siigo desde el formulario** — Datos de Google Forms validados; sin clientes duplicados por NIT.
- **Pedido al proveedor** — Plantilla de WhatsApp con el SKU del proveedor; operación registra la aceptación o el rechazo.
- **Factura en Siigo para revisión del cliente** — Sin envío a DIAN. El asesor registra la conformidad del cliente.
- **Bitácora de eventos y etapas en Mercately** — Cada evento con fecha, identificador y origen. Un estado nunca sustituye a otro: ganada no significa pagada.
- **Interruptor de pausa** — Detiene la automatización sin perder solicitudes y la reanuda en orden.
- **Enlace de pago Bold** — Para tarjeta y, si Tu merch lo decide, PSE. Vence con la cotización; webhook y consulta de estado; cada notificación se procesa una sola vez.
- **Emisión a DIAN** — Tras la aprobación del asesor, por API o desde la interfaz de Siigo según la prueba del hito 0.
- **Expediente en Drive** — Carpeta por cliente y pedido con enlaces a cotización, soporte de pago y factura.
- **Runbook y documentación** — Detener, reactivar y recuperar el servicio; mapeo de campos e identificadores; documentación de despliegue.
- **Transferencia de la Fase 1** — El equipo de Tu merch modifica una regla, revisa una excepción, encuentra una versión y rastrea un pago hasta su factura.

**Criterios de aceptación (6)**

- **A10, A11 y A12 con evidencia, y regresión de A01 a A09** — 
- **Un pedido de prueba de extremo a extremo: cotización, pago, confirmación del proveedor, factura y CRM actualizado** — 
- **Una confirmación de pago reenviada no duplica pedido ni factura** — 
- **Pausa y reactivación sin pérdida de solicitudes** — 
- **El mismo total al peso en cotización, cobro y factura, incluida la línea de envío** — 
- **Acta de aceptación de la Fase 1 firmada el 29 de octubre** — 

### D3 · Marcación Copilot, costeo y métricas

**Fechas del roadmap:** 3 – 27 nov (2026-11-03 a 2026-11-27) · **Hitos del cliente:** Hito 6

El asesor define técnica, posiciones y colores en un formulario y obtiene la cotización con marcación en segundos, como Copilot y no como agente autónomo. Tu merch ve la contribución por pedido y seis indicadores.

Momentos: Mes 2 · sujeto a aprobación · Marcación en sombra · viernes 13 de noviembre · Entrega · viernes 27 de noviembre

**Entregables (9)**

- **Tablas de marcación versionadas** — M01 a M09, declarando por tabla si contiene costo (se aplica ×1,5) o precio de venta (no se remarca), unidad de cobro, condiciones e inclusiones.
- **Motor de marcación** — Sin doble markup; kits y productos custom sin cargo duplicado; anticipo del 50 % en pedidos personalizados.
- **Formulario Copilot del asesor** — Elige la combinación válida por producto y genera la cotización borrador para revisar y enviar.
- **Ficha de producto en el PDF** — Para propuestas con personalización: descripción, características, inversión y tiempo de entrega.
- **Costeo por pedido y contribución** — Reutiliza el archivado de facturas de proveedor; contribución provisional y porcentaje de pedidos con costeo completo.
- **Reporte de seis indicadores** — Tiempo de generación, tiempo hasta envío, automatización sin intervención, cotizaciones enviadas, ganadas y perdidas, conversión a pago. Comparados con la línea base.
- **Archivado de factura en el expediente** — PDF y XML de cada factura en la carpeta del pedido, sin duplicados.
- **Evaluación de Qstomizer** — Informe de un día: qué variables se pueden extraer y cuáles no, sin integración.
- **Entrega final y transferencia de la Fase 2** — Documentación actualizada, sesión de transferencia y 30 días de soporte.

**Criterios de aceptación (4)**

- **M-A01 a M-A07 con evidencia** — 
- **La misma configuración produce el mismo precio en el formulario y en el documento** — 
- **Contribución visible en al menos diez pedidos** — 
- **El equipo de Tu merch ejecuta la transferencia sin Luup Lab** — 

## Casos de aceptación (19)

| Caso | Qué exige | Detalle | Etapa |
| --- | --- | --- | --- |
| A01 | Precio ya publicado | El precio de Shopify se usa como precio de venta. No se le añade nuevamente el markup del 40 %. | D1 |
| A02 | Pedido válido sin descuento | Stock, mínimo, precio, cantidad y totales coinciden con las fuentes. El enlace del producto abre la ficha correcta. | D1 |
| A03 | Rangos de descuento | Valores justo antes, exactamente en y justo después de cada límite de la calculadora original. | D1 |
| A04 | Pedido con varias líneas | El monto para descuento corresponde al conjunto de productos aplicables. Marcación y transporte no elevan el tramo. | D1 |
| A05 | Variantes y mínimo | Distintos colores o tallas y cantidades por debajo, en y por encima del mínimo, sin mezclar inventario de variantes. | D1 |
| A06 | Sin stock o dato faltante | El sistema conserva la solicitud, explica el bloqueo y no genera un cobro válido con información inventada. | D1 |
| A07 | Impuestos y redondeos | Líneas, descuento, impuestos y transporte coinciden en la cotización, el enlace de pago y la factura. | D1, D2 |
| A08 | Transporte | Bogotá, municipios de Sabana y otra ciudad; importes alrededor del umbral; transporte a cargo del cliente sin mostrarlo como gratis. | D1 |
| A09 | Vigencia | Vencimiento de 5 días hábiles con el calendario acordado. Una cotización vencida no cobra como si siguiera vigente. | D1, D2 |
| A10 | Flujo completo | La solicitud genera cotización, envío, pago confirmado, pedido al proveedor y factura sin recapturar información. | D2 |
| A11 | Reintentos y duplicados | Reenviar la confirmación de pago y otros eventos conserva un solo pedido y una sola factura. | D2 |
| A12 | Incidencias posteriores | Cambios de stock, rechazo del proveedor y error de facturación quedan visibles. La compra pagada no se modifica y el caso no se pierde. | D2 |
| M-A01 | Personalización incluida | Un kit o referencia custom no recibe un cargo duplicado. Las restricciones de lo incluido quedan visibles. | D3 |
| M-A02 | Costo de proveedor | El precio de marcación resulta de costo × 1,50. Se conservan costo, fuente y versión. | D3 |
| M-A03 | Tarifa de venta publicada | Si la fuente ya contiene precio de venta, el 50 % no se aplica por segunda vez. | D3 |
| M-A04 | Cambios de cantidad o tamaño | El resultado cambia según la tabla real, incluidos límites, unidades y costos fijos. | D3 |
| M-A05 | Material, técnica y posiciones | La combinación es válida para el producto y se cobran solo las posiciones o conceptos aprobados. | D3 |
| M-A06 | Arte fuera de regla | Colores no definidos, degradados o medidas ausentes producen una solicitud de información o revisión, nunca un precio inventado. | D3 |
| M-A07 | Consistencia entre canales | La misma configuración produce el mismo precio en el agente, la web y el documento. Qstomizer no duplica descuentos ni recargos. | D3 |

## Accesos e insumos del cliente (15)

| ID | Qué | Responsable | Fecha del roadmap | Bloquea |
| --- | --- | --- | --- | --- |
| dep-01 | Acceso de colaborador a Shopify con lectura de catálogo e inventario | Tecnología | 2026-10-06 | D1 |
| dep-02 | api-key de Mercately, nombres del embudo y sus 12 etapas, plan y cuota mensual, configuración de MIA y workflows de n8n que tocan Mercately | Tecnología | 2026-10-06 | D1 |
| dep-03 | Dos o tres contactos de prueba autorizados para Mercately | Tecnología | 2026-10-06 | D1 |
| dep-04 | Credenciales de la API de Siigo y ambiente de pruebas | Contabilidad | 2026-10-06 | D1 |
| dep-05 | Repositorio, usuario en n8n, hosting de la plataforma y canal de Telegram | Tecnología | 2026-10-06 | D1 |
| dep-06 | Volumen mensual aproximado de solicitudes y cotizaciones | Comercial | 2026-10-06 | D1 |
| dep-07 | Calculadora de descuentos original, modelo de cotización, plantillas de Canva y de Google Slides, PDF base | Comercial y Tecnología | 2026-10-07 | D1 |
| dep-08 | 10 conversaciones históricas anonimizadas y 5 cotizaciones reales | Tecnología | 2026-10-07 | D1 |
| dep-09 | Carpeta del expediente en Drive y formulario de facturación con su hoja de respuestas | Brayan | 2026-10-07 | D2 |
| dep-10 | Llaves de integración de Bold y ambiente de pruebas | Brayan y contabilidad | 2026-10-13 | D2 |
| dep-11 | Lista de proveedores, número de WhatsApp de cada uno y formato actual del pedido | Operación | 2026-10-13 | D2 |
| dep-12 | Dos o tres clientes reales para la lista de permitidos | Comercial | 2026-10-16 | D2 |
| dep-13 | Procedimiento de contabilidad para emitir facturas reales a DIAN durante el piloto | Contabilidad | 2026-10-16 | D2 |
| dep-15 | Comercial y contabilidad disponibles unas dos horas por día para las pruebas de aceptación | Brayan | 2026-10-22 | D2 |
| dep-14 | Tablas de marcación M01 a M09 con nombre, responsable, versión, costo o venta, unidad, condiciones y restricciones | Operación y producción | 2026-10-23 | D3 |

## Decisiones pendientes del cliente (10)

| ID | Decisión | Responsable | Fecha del roadmap | Bloquea |
| --- | --- | --- | --- | --- |
| dec-01 | IVA y redondeo por concepto | Contabilidad | 2026-10-07 | D1 |
| dec-02 | Transporte: base del umbral de 2.000.000 y municipios cubiertos de Sabana | Brayan | 2026-10-07 | D1 |
| dec-03 | Vigencia: calendario de festivos y hora de vencimiento | Brayan | 2026-10-07 | D1 |
| dec-04 | Etapa que dispara la cotización y etapas destino en el embudo | Tecnología y comercial | 2026-10-07 | D1 |
| dec-05 | Siigo como registro formal y Google Slides como documento al cliente | Brayan | 2026-10-07 | D1 |
| dec-06 | Pagos: métodos automatizados, anticipo, vencimiento, devoluciones y cobro de kits | Brayan y contabilidad | 2026-10-09 | D2 |
| dec-07 | Factura: evento de emisión y transporte facturado después | Contabilidad | 2026-10-09 | D2 |
| dec-08 | Reserva de stock y concurrencia antes del pago | Brayan y operación | 2026-10-13 | D2 |
| dec-09 | Pedido al proveedor: canal, confirmación y rechazo | Operación | 2026-10-13 | D2 |
| dec-10 | Kits y custom, marcación, Qstomizer, documentos y costeo | Brayan y producción | 2026-10-23 | D3 |

## Fuera del alcance (6)

- **Entrada por correo o web** — El asesor crea la negociación en Mercately y la solicitud entra al mismo flujo, con el mismo precio.
- **Verificación de stock en las API de proveedores** — Disponible como opcional del mes 2 para los dos proveedores que exponen API.
- **Selección automática del proveedor** — La asignación sigue la operación de Tu merch.
- **Cotizador web o Qstomizer como canal de venta** — El checkout está apagado por decisión comercial. Qstomizer solo se evalúa en el mes 2.
- **Previsualización del logo sobre el producto** — Construcción aparte de render de imagen, no reutiliza el motor de precio.
- **Fase 3: integración de proveedores** — Los 890 proveedores quedan para una fase posterior.

## Hitos del roadmap

| Fecha | Hito |
| --- | --- |
| 2026-10-01 | Propuesta |
| 2026-10-05 | Kickoff |
| 2026-10-14 | D1 sombra |
| 2026-10-21 | D2 |
| 2026-10-23 | Tablas |
| 2026-10-29 | Producción |
| 2026-11-27 | Entrega D3 |

Festivos declarados en el roadmap: 2026-10-12, 2026-11-02, 2026-11-16. **Faltan el 8 y el 25 de diciembre de 2026**, que sí entran en juego si D3 se corre a diciembre según ADR-001.

Fecha de salida declarada en el roadmap: **2026-10-29**.
