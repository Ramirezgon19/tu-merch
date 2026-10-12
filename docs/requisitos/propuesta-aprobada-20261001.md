# Cotizador automático — Respuesta de Luup Lab al paquete de estimación

**Para:** Tu merch Productos Publicitarios S.A.S. — Brayan Daniel Ortega Bayona · Miguel Fabián Tusso
**De:** Luup Lab — Alejandro Gil Rivera · David Ramírez González · Juan Felipe Beltrán
**Fecha:** 1 de octubre de 2026 · **Validez:** hasta el viernes 30 de octubre de 2026
**Confidencialidad:** cubierto por el NDA firmado el 23 de septiembre de 2026.

---

## Resumen

Leímos completos los dos documentos del paquete: la *Definición funcional y guía de integración* (v1.0, 19/09) y el *Anexo técnico mínimo para estimación* (v1.0, 24/09). Aceptamos la Fase 1 con el alcance completo de la sección 05 —cotización, pago, pedido al proveedor y factura electrónica— con salida en producción el jueves 29 de octubre de 2026, por 5.000.000 COP. La ejecutamos en dos despliegues que siguen sus hitos 0 a 5: uno en modo sombra el 14 de octubre y otro en lista de permitidos el 21 de octubre, con la semana del 22 al 28 como piloto con revisión humana de todas las cotizaciones. La Fase 2 (marcación) y los módulos de expediente, costeo y métricas —su hito 6— los proponemos como un segundo mes a precio cerrado de 5.000.000 COP, que arranca el 3 de noviembre si las tablas de marcación se entregan el 23 de octubre. Este documento responde a cada fila de la tabla "Lo que esperamos recibir en la propuesta" y a las seis preguntas técnicas del anexo, y termina con la lista fechada de lo que necesitamos de Tu merch para que el 29 de octubre se sostenga.

---

## 1. Cómo leímos su paquete

Su definición y nuestro enfoque coinciden en lo esencial: la velocidad de la cotización decide el cierre; Shopify es la única fuente del catálogo y del precio, y no se escribe en ella; la revisión humana es un control de arranque y de excepciones, no un paso permanente; un solo motor de cálculo sirve a todos los canales; y la marcación es una segunda fase que conserva las reglas de la primera. Su anexo técnico mejora nuestros supuestos: el mínimo de compra ya existe en el metacampo `custom.cantidad_minima`, el precio de Shopify es sin IVA, la API de Mercately está confirmada contra su especificación, y su plataforma en FastAPI, su instancia de n8n, su extractor en Gemini y su bot de Telegram son cimientos que reutilizamos en lugar de construirlos.

La Fase 1 incluye todo lo que su definición pide: la cotización formal y la factura en Siigo, la verificación del pago, el pedido al proveedor, el flujo de aprobación previo a DIAN, las plantillas de WhatsApp aprobadas por Meta, la detección de solicitudes sin webhooks, doce casos de aceptación con evidencia, la salida por modos y el paquete de entrega. La marcación queda en el segundo mes porque sus insumos —las tablas M01 a M09— no se han entregado, y su propio documento (§24) dice que sin tabla no hay regla definitiva.

---

## 2. Alcance por hito

Sus siete hitos se agrupan en tres despliegues. La tabla dice qué cierra cada hito, cuándo y con qué casos.

| Hito de Tu merch (§20) | Qué lo cierra | Fecha | Despliegue | Casos |
|---|---|---|---|---|
| 0. Validar accesos y dependencias | Evidencia de cada acceso y prueba de concepto por integración; lista de limitaciones encontradas | Jueves 8/10 | D1 | — |
| 1. Cerrar reglas y datos | Mapeo de campos e identificadores, calculadora original validada, decisiones de IVA, transporte, vigencia y etapas registradas | Viernes 9/10 | D1 | — |
| 2. Construir Fase 1 de cotización | Cotización correcta en Siigo y PDF, en modo sombra | Miércoles 14/10 | **D1 · Cotizador en sombra** | A01–A09 en cálculo y documento |
| 3. Conectar el cierre completo | Envío, pago, pedido al proveedor y factura borrador, en lista de permitidos | Miércoles 21/10 | **D2 · Cierre digital** | A10; A07 y A09 en cobro y factura |
| 4. Piloto con revisión humana | Todos los casos ejecutados con la persona comercial y contabilidad; enlace Bold; emisión DIAN | Jueves 22 – miércoles 28/10 | D2 | A11, A12; regresión A01–A10 |
| 5. Salida Fase 1 | Producción con monitoreo, runbook y transferencia; acta de aceptación | Jueves 29/10 | D2 | — |
| 6. Fase 2 y módulos | Marcación como Copilot, costeo, métricas, evaluación de Qstomizer | Martes 3/11 → viernes 27/11 | **D3** (mes 2) | M-A01–M-A07 |

### D1 · Cotizador en sombra — 14 de octubre

Desde que se dispara, una solicitud cualificada produce en menos de dos minutos una cotización correcta registrada en Siigo y un PDF con el formato de su plantilla, listos para que la persona comercial los revise y los envíe. Nada sale al cliente final de forma automática.

Incluye: evidencia de cada acceso e integración (Shopify en lectura; Mercately crear y mover negociación; Siigo cliente, producto, cotización con URL pública y factura en ambiente de pruebas); la solicitud estructurada sobre su extractor de Gemini, extendido para capturar variante o color, dirección, fecha requerida y modalidad, con manejo de ambigüedad que pide solo lo faltante; el motor de cálculo dentro de su plataforma: lectura de Shopify, validación de mínimo y stock por variante, calculadora de descuentos reproducida desde el archivo original con pruebas en cada límite de tramo, IVA del 19 %, transporte (Bogotá y Sabana gratis por encima de 2.000.000; otras ciudades como línea de envío con valor definido por el asesor o "a cargo del cliente"), vigencia de 5 días hábiles con festivos de Colombia, y un snapshot versionado de cada cotización (precio tomado, versión de la calculadora, disponibilidad consultada); creación del producto en Siigo bajo demanda con el código de la variante y de la cotización en Siigo; consecutivo interno que continúa su numeración actual (parametrizado, hoy alrededor de 4.000) en el documento y guardado junto al número que asigne Siigo; PDF generado desde la plantilla de Google Slides con enlaces a la ficha de cada producto; registro de ambos enlaces en la negociación; cola de revisión para el asesor; errores al bot de Telegram; modo sombra; repositorio con integración continua; y la hoja de línea base de operación (volumen, tiempo manual, tasa de revisión, motivos de bloqueo) que pide §19, capturada desde el 6 de octubre para poder comparar después.

Los kits y productos con personalización incluida se cotizan en Fase 1 al precio de Shopify, sin cargo adicional, y pasan a revisión del asesor para definir el cobro (total o anticipo, según la decisión de la sección 5); su cierre sin revisión entra en el mes 2.

Criterio de cierre: A01 a A09 con evidencia en cálculo y documento; las cinco cotizaciones reales de muestra reproducidas al peso; cero escrituras en Shopify; snapshot recuperable por identificador.

### D2 · Cierre digital — 21 de octubre en lista de permitidos, 29 de octubre en producción

Un pedido estándar sin marcación recorre cotización, envío, pago, pedido al proveedor y factura sin volver a capturar información.

Al 21 de octubre, en lista de permitidos con contactos de prueba y dos o tres clientes reales, y con revisión del asesor antes de cada envío, como pide la salida controlada de §20: envío de la cotización por plantilla aprobada al aprobarla en la cola (mientras Meta aprueba, el asesor la envía desde la conversación con el texto listo); confirmación de pago idempotente con soporte para Llave Bre-B, PSE por Rappipay y transferencia, que son los tres métodos sin costo que ofrece Tu merch; revalidación de stock antes de confirmar el cobro y regla de reserva acordada; datos fiscales del formulario de Google validados y creados en Siigo sin clientes duplicados; pedido al proveedor por plantilla de WhatsApp con el SKU del proveedor, y registro de su aceptación o rechazo por operación mediante un formulario o comando; factura en Siigo sin envío a DIAN enviada al cliente para revisión, cuya conformidad registra el asesor; movimientos de etapa en Mercately y bitácora de eventos con fecha, identificador y origen, sin usar un estado como sustituto de otro; interruptor para pausar la automatización sin perder solicitudes.

Del 22 al 28 de octubre, durante el piloto: enlace de pago Bold para tarjeta —y para PSE si Tu merch decide llevarlo por Bold— con vencimiento igual a la vigencia, notificación por webhook y consulta de estado, e idempotencia por referencia; emisión a DIAN tras la aprobación del asesor; expediente en Drive con la carpeta por cliente y pedido y los enlaces a cotización, soporte de pago y factura (el archivado del PDF y el XML de la factura se completa en el mes 2); runbook para detener, reactivar y recuperar el servicio; mapeo de campos e identificadores; documentación de despliegue; y una sesión de transferencia en la que su equipo modifica una regla, revisa una excepción, encuentra la versión de una cotización y rastrea un pago hasta su factura. El autoenvío sin revisión previa se activa el 29 de octubre, solo para los casos que hayan pasado el piloto. La Fase 1 queda operable por Tu merch sin depender del mes 2.

Criterio de cierre: A10, A11 y A12 con evidencia y regresión de A01 a A09; un pedido de prueba de extremo a extremo con cotización, pago, confirmación del proveedor, factura en el ambiente aprobado y CRM actualizado; reenvío de una confirmación de pago sin duplicar pedido ni factura; pausa y reactivación sin pérdida; el mismo total al peso en cotización, cobro y factura, incluida la línea de envío. Acta de aceptación de Fase 1 el 29 de octubre.

### D3 · Marcación Copilot, costeo y métricas — 3 al 27 de noviembre (mes 2)

El asesor define técnica, posiciones y colores en un formulario y obtiene la cotización con marcación en segundos, como Copilot y no como agente autónomo, según la preferencia de §11. Tu merch ve la contribución por pedido y los seis indicadores básicos.

Incluye: carga versionada de las tablas M01 a M09 declarando por tabla si contiene costo (se aplica ×1,5) o precio de venta (no se remarca), unidad de cobro, condiciones e inclusiones; motor de marcación sin doble markup, con kits y productos custom sin cargo duplicado y anticipo del 50 % en el cobro de pedidos personalizados; formulario interno en su plataforma para que el asesor elija la combinación válida; ficha de producto en el PDF para propuestas con personalización; costeo por pedido reutilizando su archivado de facturas de proveedor, con contribución provisional y porcentaje de pedidos con costeo completo; reporte de seis indicadores de §19 sobre la bitácora de eventos (tiempo de generación, tiempo hasta envío, automatización sin intervención, cotizaciones enviadas, tasa de ganadas y perdidas, conversión a pago), comparados con la línea base de octubre; archivado de PDF y XML de factura en el expediente; informe de evaluación de Qstomizer de un día (qué variables se pueden extraer y cuáles no, sin integración); paquete de entrega final y transferencia de la Fase 2; 30 días de soporte.

Criterio de cierre: M-A01 a M-A07 con evidencia; la misma configuración produce el mismo precio en el formulario y en el documento; contribución visible en al menos diez pedidos; su equipo ejecuta las tareas de transferencia sin nosotros.

### Alcance que queda explícitamente fuera y por qué

La entrada de solicitudes es única, por Mercately: una solicitud que llegue por correo o por la web la crea el asesor como negociación y desde ahí entra al mismo flujo (§07 pide que el canal no cambie el precio, y así se garantiza). La doble verificación de stock contra las API de los dos proveedores que la exponen (Anexo §3.3) no está en la Fase 1; la estimamos como opcional del mes 2 en la sección 6. Quedan fuera la selección automática del proveedor, el cotizador web o Qstomizer como canal de venta, la previsualización del logo sobre el producto y la Fase 3 de integración de proveedores; cualquiera puede cotizarse aparte cuando Tu merch lo decida. Sobre las aperturas de cotización (§16 y §19): no hemos verificado que Siigo exponga eventos de apertura por API; el indicador se reportará con su cobertura real y, si es cero, se dirá así, como pide §19.

---

## 3. Decisiones técnicas y respuestas a las seis preguntas del anexo

**Dónde corre el motor y qué cuesta operarlo.** El motor de cálculo se construye como un módulo de dominio dentro de su plataforma en FastAPI y PostgreSQL, usando su bandeja de salida con idempotencia y sus modos off, shadow, allowlist y live; el hito 0 incluye la productivización mínima que la plataforma necesite para salir del modo sombra (servicio, worker, secretos). n8n orquesta la detección de solicitudes y los webhooks entrantes, y reporta errores a su bot de Telegram. El costo adicional de infraestructura es cero mientras la plataforma corra donde corre hoy; si hay que provisionar un servidor productivo, el rango está en la sección 6. La entrega se hace en su repositorio de GitHub, con los workflows de n8n exportados como JSON, las credenciales en su gestor de secretos y sin datos personales ni fiscales en URLs ni registros, como exige el Anexo §4.6.

**Cómo se detectan solicitudes nuevas sin webhooks.** Lo resolvemos en los dos primeros días del hito 0 con pruebas en su cuenta, usando contactos de prueba autorizados. Tres rutas, en orden de preferencia: si la API permite listar negociaciones por etapa, un sondeo cada 10 minutos en horario hábil, que consume unas 1.300 llamadas al mes y que confirmaremos contra la cuota de su plan el 6 de octubre; si el agente MIA o los chatbots de Mercately pueden invocar una URL al completar la cualificación, ese enganche; y como mínimo garantizado desde el primer despliegue, un comando del asesor desde el bot de Telegram o desde un formulario interno, con el identificador de la negociación. La latencia de detección es de hasta 10 minutos con sondeo y de segundos en las otras dos rutas; el cálculo y el documento tardan menos de dos minutos en cualquiera de ellas.

**Prueba de concepto con Siigo: alcance y duración.** Ya integramos Siigo en otro proyecto (cliente fiscal, cotización y factura), así que la prueba no parte de cero: en los tres primeros días hábiles tras recibir credenciales entregamos evidencia de crear y actualizar un cliente fiscal, crear un producto con el código de la variante de Shopify sin duplicar referencias, crear una cotización y obtener su enlace público, y crear una factura sin envío a DIAN en el ambiente de pruebas. Lo que queda por demostrar con su cuenta es el envío posterior a DIAN por API; si no está disponible, la emisión se hace desde la interfaz de Siigo con el mismo control de aprobación, y lo decimos con evidencia antes de comprometer el flujo. La conformidad del cliente con el borrador de factura llega por WhatsApp y la registra el asesor en la cola de revisión; no dependemos de un evento entrante de Mercately, que no existe.

**Pagos con Bold.** Bold expone una API de enlaces de pago con monto cerrado, referencia única, fecha de vencimiento, notificación por webhook y consulta de estado. La usamos para tarjeta y, si Tu merch decide moverlo desde Rappipay, para PSE; la referencia del enlace es el identificador de la cotización y su versión, el vencimiento es la vigencia, y cada notificación repetida se procesa una sola vez. Los pagos por Llave Bre-B, PSE por Rappipay y transferencia se confirman con la ruta manual idempotente con soporte, que construimos primero; en el hito 0 verificamos si Bold incluye la Llave dentro del enlace y, si lo hace, la sumamos a la verificación automática. La prueba de concepto de Bold se hace en la primera semana con una cuenta de pruebas propia y se repite con sus llaves el 13 de octubre.

**Plantillas de WhatsApp.** Como la API solo envía plantillas aprobadas por Meta, el flujo necesita ocho —cotización lista, faltan datos, sin disponibilidad o mínimo no alcanzado, recordatorio de pago, datos de facturación, pedido al proveedor, factura para revisión y aviso de vencimiento— más las que deriven de las decisiones de pago y factura, hasta diez. Las redactamos y entregamos el 9 de octubre para que la persona comercial valide el tono; su administrador de Mercately las somete el 14, una vez tomadas las decisiones de pago y factura de las que dependen dos de los textos; mientras Meta responde, el asesor envía el mensaje desde la conversación con el texto listo. Acordaremos con Tecnología la regla para apagar el agente MIA y los chatbots en una negociación cuando el motor toma el control.

**Estrategia de pruebas sin contaminar el CRM ni la tienda.** Shopify solo se lee. En Mercately trabajamos con contactos de prueba propios autorizados desde el hito 0, marcamos las negociaciones de prueba en un campo personalizado y, antes de escribir el sondeo, inventariamos los workflows de n8n que ya tocan Mercately para no procesar dos veces la misma solicitud. Siigo y Bold se prueban en sus ambientes de pruebas; la factura solo se emite a DIAN en el piloto con el procedimiento que apruebe contabilidad. Toda la automatización arranca en modo sombra —registra lo que haría, sin efectos externos—, pasa a lista de permitidos con revisión del asesor antes de cada envío, y solo después de que los casos acordados tengan evidencia se activa en producción, con un interruptor para pausarla sin perder solicitudes. Usamos agentes de código sobre su repositorio con revisión humana de cada cambio, y el extractor corre en Gemini con la cuenta de Tu merch; ambos figuran en la lista de proveedores tecnológicos que entregaremos el 9 de octubre para la autorización marco prevista en el NDA.

**Decisión que pedimos aprobar: Siigo como registro, Google Slides como documento.** La cotización en Siigo aporta consecutivo, trazabilidad, base para la factura y un enlace público, pero su formato no reproduce la portada con el logo del cliente, los enlaces a la ficha de cada producto ni la página institucional que exige §13. Proponemos que cada cotización exista en los dos lugares con las mismas líneas y totales, generados desde el mismo snapshot: en Siigo como registro formal y origen de la factura, y como PDF generado desde la plantilla de Google Slides que Tu merch diseñó en junio, con el formato de su plantilla de Canva y la vigencia de 5 días hábiles. Es la alternativa que §06 y §20 piden presentar antes de construir; está incluida en los 5.000.000 COP y no tiene costo adicional para Tu merch.

---

## 4. Cronograma contra el 29 de octubre

| Fecha | Hito |
|---|---|
| Jueves 1 – viernes 2 de octubre | Entrega de esta respuesta; reunión de cierre y kickoff propuesta para el lunes 5 |
| Lunes 5 – martes 6 de octubre | Firma, anticipo, grupo de comunicación, entrega de accesos del hito 0, repositorio y backlog |
| Miércoles 7 – martes 13 de octubre (4 días hábiles) | Construcción de D1; pruebas de concepto de Siigo y de detección los dos primeros días |
| **Miércoles 14 de octubre** | **D1 en modo sombra**; demostración con la persona comercial y Brayan |
| Jueves 15 – martes 20 de octubre (4 días hábiles) | Construcción de D2; plantillas sometidas a Meta el 14 |
| **Miércoles 21 de octubre** | **D2 en lista de permitidos**; demostración |
| Jueves 22 – miércoles 28 de octubre | Piloto con revisión humana; enlace Bold, emisión DIAN, runbook y transferencia de Fase 1. El viernes 23 es la fecha límite para las tablas M01–M09 y para la decisión sobre el mes 2 |
| **Jueves 29 de octubre** | **Fase 1 en producción**; acta de aceptación |
| Viernes 30 de octubre – viernes 27 de noviembre | 30 días de soporte de la Fase 1 |
| Martes 3 – viernes 27 de noviembre | D3 (mes 2); motor de marcación en sombra el viernes 13; entrega el viernes 27 |
| Lunes 30 de noviembre – miércoles 30 de diciembre | 30 días de soporte de la Fase 2 |

Los festivos del 12 de octubre, 2 de noviembre y 16 de noviembre están descontados de las ventanas de construcción.

**Camino crítico.** Accesos del hito 0 el 6 de octubre → prueba de concepto de Siigo el 8 → motor y cotización el 14 → plantillas sometidas el 14 → cierre digital mínimo el 21 → piloto → 29. Cada día hábil de retraso en los accesos mueve D1 y D2 un día. La semana de piloto tiene holgura para hasta dos días de retraso sin mover el 29 de octubre; a partir del tercero, el enlace Bold o la emisión a DIAN por API pasan a la primera semana de noviembre y el 29 sale con cotización, pago confirmado manualmente, pedido al proveedor y factura borrador.

**Si Siigo se retrasa.** Si las credenciales no llegan el 6 de octubre, D1 sale con el PDF de Slides como único documento y el registro en Siigo se incorpora en D2. La factura sí exige Siigo: un retraso posterior al 13 de octubre mueve la emisión de facturas al piloto, y si pasa del 20, la salida del 29 se limita a cotización, pago y pedido, con la factura entrando la semana siguiente. Lo diríamos con evidencia el mismo día en que se conozca.

**Si los pagos se retrasan.** La confirmación manual idempotente no depende de Bold y cubre los tres métodos actuales sin costo; si las llaves de Bold no llegan el 13 de octubre, la salida del 29 se hace sin enlace de pago automático y este entra en cuanto haya llaves, sin cambiar el resto del flujo.

**Si Meta demora las plantillas.** El asesor envía desde la conversación con el texto listo; el autoenvío se activa el día en que cada plantilla quede aprobada.

---

## 5. Dependencias de Tu merch

Ningún acceso viaja por correo ni por el grupo de comunicación: se entregan por el canal seguro que defina Tecnología.

| Qué necesitamos | Fecha | Responsable |
|---|---|---|
| Acceso de colaborador a Shopify con lectura de catálogo e inventario | Martes 6/10 | Tecnología |
| api-key de Mercately, nombres exactos del embudo y sus 12 etapas, plan contratado y cuota mensual, configuración del agente MIA, lista de workflows de n8n que tocan Mercately | Martes 6/10 | Tecnología |
| Contactos de prueba propios autorizados para Mercately (dos o tres números) | Martes 6/10 | Tecnología |
| Credenciales de la API de Siigo y ambiente o empresa de pruebas | Martes 6/10 | Tu merch y contabilidad |
| Acceso al repositorio, usuario en n8n, dónde corre la plataforma (hosting, base de datos, gestor de secretos), canal de Telegram | Martes 6/10 | Tecnología |
| Volumen mensual aproximado de solicitudes y cotizaciones | Martes 6/10 | Comercial |
| Copia de la calculadora de descuentos original (.xlsx), del «Módelo Cotizaciones.pdf», de la plantilla de Canva editable, del PDF base limpio y de la plantilla de Google Slides de junio | Miércoles 7/10 | Comercial y Tecnología |
| 10 conversaciones históricas anonimizadas y 5 cotizaciones reales | Miércoles 7/10 | Tecnología |
| Carpeta de Drive del expediente, formulario de datos de facturación y su hoja de respuestas | Miércoles 7/10 | Tu merch |
| Llaves de integración de Bold y ambiente de pruebas; decisión de qué métodos se automatizan | Martes 13/10 | Tu merch y contabilidad |
| Lista de proveedores, número de WhatsApp de cada uno y formato actual del pedido | Martes 13/10 | Operación |
| Dos o tres clientes reales para la lista de permitidos del piloto | Viernes 16/10 | Comercial |
| Procedimiento aprobado por contabilidad para emitir facturas reales a DIAN durante el piloto | Viernes 16/10 | Contabilidad |
| Tablas de marcación M01–M09 con nombre de archivo, responsable, versión, si son costo o venta, unidad de cobro, condiciones y restricciones | Viernes 23/10 | Operación y producción |

Decisiones de §26 que necesitamos con fecha, cada una con un responsable de su lado:

| Decisión | Responsable en Tu merch | Fecha |
|---|---|---|
| IVA y redondeo por concepto | Contabilidad | Miércoles 7/10 |
| Transporte: base del umbral de 2.000.000 y municipios cubiertos de Sabana | Brayan | Miércoles 7/10 |
| Vigencia: calendario de festivos y hora de vencimiento | Brayan | Miércoles 7/10 |
| Etapa que dispara la cotización y etapas destino en el embudo | Tecnología y comercial | Miércoles 7/10 |
| Siigo como registro y Slides como documento (sección 3) | Brayan | Miércoles 7/10 |
| Pagos: métodos automatizados, anticipo, vencimiento, devoluciones; cobro de kits con personalización incluida | Brayan y contabilidad | Viernes 9/10 |
| Factura: evento de emisión y tratamiento del transporte facturado después | Contabilidad | Viernes 9/10 |
| Mínimos y stock: reserva y concurrencia antes del pago | Brayan y operación | Martes 13/10 |
| Pedido al proveedor: canal, confirmación y rechazo | Operación | Martes 13/10 |
| Kits y custom, marcación, Qstomizer, documentos y costeo | Brayan y producción | Viernes 23/10 (para el mes 2) |

Para las pruebas de aceptación necesitamos a la persona comercial y a contabilidad disponibles entre el 22 y el 28 de octubre, unas dos horas por día.

---

## 6. Inversión

Valores en pesos colombianos, sin IVA. Los honorarios se facturan bajo el esquema de persona natural, con un contrato de prestación de servicios por honorarios que acompaña esta propuesta.

**Mes 1 — Fase 1 completa (D1 + D2)**

| Hito | Contenido | Valor |
|---|---|---|
| Hitos 0 y 1 | Validación de accesos, pruebas de concepto con evidencia, productivización mínima de la plataforma, cierre de reglas y datos, mapeo de campos | 800.000 |
| Hito 2 | Cotización automática: motor, calculadora, Siigo, documento, registro en CRM, modo sombra | 1.700.000 |
| Hito 3 | Cierre digital: envío, pagos, cliente fiscal, pedido al proveedor, factura, bitácora | 1.900.000 |
| Hitos 4 y 5 | Piloto, salida en producción, runbook, documentación y transferencia de Fase 1 | 600.000 |
| **Total mes 1** | | **5.000.000** |

**Mes 2 — Fase 2 y módulos complementarios (D3), a precio cerrado**

| Módulo | Contenido | Valor |
|---|---|---|
| Tablas y motor de marcación | Carga versionada de M01–M09, motor sin doble markup, kits y custom, anticipo | 2.000.000 |
| Copilot y documento | Formulario interno para el asesor, ficha de producto en el PDF | 1.200.000 |
| Costeo y métricas | Costeo por pedido, contribución provisional, reporte de seis indicadores | 1.000.000 |
| Cierre | Evaluación de Qstomizer, archivado en expediente, entrega final y transferencia | 800.000 |
| **Total mes 2** | | **5.000.000** |
| Opcional | Doble verificación de stock contra las API de los dos proveedores que la exponen (Anexo §3.3), 3 días | 700.000 |

Condiciones del mes 2: el alcance es el descrito en D3, con nueve tablas de marcación; las tablas se entregan el 23 de octubre y la decisión de continuar se toma esa misma semana, después de ver D2 funcionando. Fuera de ese alcance o de esa fecha, el trabajo se cotiza por tiempo y materiales según disponibilidad.

**Costo mensual de operación**

| Concepto | Rango mensual | Nota |
|---|---|---|
| Infraestructura del motor y la orquestación | 0 – 120.000 COP | Corre en la plataforma y el n8n de Tu merch; el rango aplica solo si hay que provisionar un servidor productivo |
| IA de extracción (Gemini, cuenta de Tu merch) | 40.000 – 160.000 COP | Depende del volumen mensual de solicitudes, por confirmar |
| API de Mercately | Según el plan contratado | El diseño consume unas 1.300 llamadas de sondeo al mes más 3 a 5 por cotización; se confirma contra la cuota el 6/10 |
| Bold | Comisión por transacción | Según el método habilitado; decisión comercial de Tu merch |
| Siigo, Mercately, Qstomizer, n8n, Google Workspace | Ya contratados | Sin costo adicional |
| Soporte de Luup Lab | Incluido 30 días por fase; después, 5.000.000 COP mensuales | Retainer opcional de soporte y evolución, cancelable mes a mes; alcance acordado al cierre de la Fase 1 |

Los rangos de infraestructura e IA son estimaciones que se confirman con el volumen real de solicitudes del primer mes.

**Forma de pago.** 50 % a la firma y 50 % con el acta de aceptación del 29 de octubre. Para el mes 2, 50 % al inicio (3 de noviembre) y 50 % con la entrega (27 de noviembre). Validez de esta propuesta: hasta el viernes 30 de octubre de 2026. El cronograma asume el kickoff el lunes 5 de octubre y los accesos el martes 6; si el arranque ocurre después, el cronograma se desplaza día por día y la fecha de salida se recalcula.

---

## 7. Equipo y soporte

El equipo son tres personas. Alejandro Gil Rivera dirige el proyecto, responde por la calidad y la documentación y es el interlocutor único para Tu merch. David Ramírez González y Juan Felipe Beltrán construyen el motor de cálculo y las integraciones con Shopify, Mercately, Siigo, Bold y n8n; uno de ellos ya integró Siigo en un proyecto anterior. Trabajamos sobre un mismo repositorio con agentes de código, y cada cambio pasa por revisión humana antes de llegar a su plataforma.

La comunicación diaria va por un grupo de WhatsApp con las personas de Tu merch que el proyecto necesita: Tecnología, Brayan, la persona comercial, contabilidad y operación. Cada decisión tomada en el grupo queda registrada el mismo día como issue en el repositorio, que es la trazabilidad del proyecto. Publicamos un estado diario de tres líneas y hacemos una demostración en cada despliegue.

Tiempos de respuesta: durante la construcción y el piloto, cuatro horas hábiles para cualquier bloqueo; después de la salida en producción y durante los 30 días de soporte, cuatro horas hábiles para incidentes que detengan la generación de cotizaciones o el cobro, y un día hábil para el resto. Cuando una integración falle en producción, el flujo pasa a revisión manual sin perder la solicitud, el error se reporta a Telegram con su causa y queda registrado en la bitácora con responsable y resolución, como pide §17.

A cambio necesitamos de Tu merch: los accesos en las fechas de la sección 5, un responsable con fecha por cada decisión, revisión de los pull requests que toquen su infraestructura en 24 horas hábiles o autorización expresa para desplegar con revisión posterior, y la participación de la persona comercial y de contabilidad en las pruebas de aceptación.

---

## 8. Riesgos y mitigación

| Riesgo | Impacto | Mitigación |
|---|---|---|
| Los accesos llegan después del 6 de octubre | Mueve D1 y D2 día por día | Hitos internos medidos en días hábiles tras los accesos; escenarios de la sección 4 |
| Credenciales de Siigo dependen de contabilidad | Sin cotización en Siigo en D1; sin factura si pasa del 13 | Slides es el documento desde D1; registro en Siigo entra en D2; escenarios en la sección 4 |
| Mercately: sin webhooks, cuota del plan, una sola api-key de producción, sin borrado, con MIA y n8n activos | Detección lenta o costosa; pruebas con huella; doble procesamiento | Sondeo en horario hábil o enganche a MIA; comando del asesor como mínimo; contactos de prueba marcados; inventario de workflows; regla de apagado de MIA |
| Aprobación de plantillas por Meta | Sin autoenvío hasta la aprobación | Redacción el 9, sometimiento el 14, envío desde la conversación con texto listo mientras tanto |
| Pagos que hoy no pasan por un enlace verificable (Bre-B, PSE por Rappipay, transferencia) | La verificación automática cubre solo tarjeta y lo que Tu merch decida llevar a Bold | Confirmación manual idempotente para los tres métodos sin costo; verificación en el hito 0 de si Bold incluye la Llave en el enlace |
| Plataforma en modo sombra, no productivizada | Horas de despliegue y cuello de botella en revisiones | Productivización mínima en el hito 0; acuerdo de revisión en 24 horas hábiles |
| Calculadora y modelo de cotización pendientes de recibir | Sin pruebas de tramos (A03) | Solicitados para el 7 de octubre |
| Tablas M01–M09 no entregadas | El mes 2 no puede arrancar el 3 de noviembre | Fecha límite del 23 de octubre escrita en esta propuesta |
| Idempotencia y reintentos en pagos, pedidos y facturas | Duplicados | Bandeja de salida con llave de idempotencia; ante respuesta incierta, revisión manual, nunca reintento a ciegas; evidencia en A11 |
| Proveedores tecnológicos y datos personales bajo el NDA | Incumplimiento formal de la autorización marco | Lista de proveedores (Gemini, agentes de código, Bold, Google Workspace) entregada el 9 de octubre para aprobación |

---

## 9. Próximos pasos

Proponemos una reunión de cierre y kickoff el lunes 5 de octubre, de una hora, con Brayan, Miguel y la persona comercial: confirmamos el alcance de la Fase 1, la decisión sobre Siigo y Slides, la fecha de decisión del mes 2 y el calendario de accesos; firmamos y abrimos el grupo de comunicación ese mismo día. Los accesos del hito 0 llegan el martes 6 y la construcción empieza el miércoles 7.

Luup Lab — hola@luuplab.com — luuplab.com
