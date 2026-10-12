# CLAUDE.md — Cotizador automático · Tu Merch × Luup Lab

Reglas que cualquier persona y cualquier agente de código debe respetar antes de tocar este repositorio. `AGENTS.md` tiene las mismas reglas para agentes que leen ese nombre.

## 0. Al abrir una sesión

1. Lee `docs/requisitos/base-proyecto.md`. Es la base del proyecto y la autoridad interna: requisitos, arquitectura propuesta, los workflows WF-00 a WF-14, el contrato de datos, los pendientes P0/P1/P2 y el plan de aceptación. Su encabezado dice qué versión es y qué no está aprobado todavía.
2. Lee `docs/decisiones/` completo. Son pocos archivos y deciden cosas que la base deja abiertas.
3. Lee el issue que vas a trabajar. **Nada sin issue**, y el criterio de terminado del issue es el contrato.
4. Para una regla de negocio, la cadena de autoridad está en la sección 2 de este archivo. No resuelvas por conveniencia una contradicción entre fuentes: eso se registra, no se decide en código.

## 1. Qué es este sistema

Convierte una solicitud recibida por WhatsApp en una cotización correcta, registrada formalmente y con el documento de la empresa, y luego lleva el pedido estándar sin marcación por pago, pedido al proveedor y factura electrónica con sus aprobaciones fiscales. La Fase 2 añade marcación como copiloto del vendedor.

Estado real: **diseño**. No hay workflows implementados ni despliegue. El siguiente entregable recomendado por la base es el diseño detallado de WF-01 a WF-06 con el contrato JSON y el manejo de excepciones.

## 2. Autoridad de las fuentes, en orden

1. **Paquete de estimación v1** del cliente (funcional de Brayan del 19/09 y anexo técnico de Miguel del 24/09): reglas de negocio y casos de aceptación A01–A12.
2. **Guía técnica de integración v2** del cliente, del 08/10: entorno, límites de API y convivencia. Reemplaza expresamente a la v1, que no se implementa.
3. **Roadmap aprobado del 01/10/2026** (`docs/requisitos/roadmap-aprobado-20261001.md`, con el HTML original al lado): el artefacto que Tu Merch aprobó. Etapas K/D1/D2/D3 con sus entregables y criterios, los 19 casos, las dependencias `dep-01`–`dep-15`, las decisiones `dec-01`–`dec-10` y las exclusiones. **Manda en materia contractual.** La propuesta del mismo día lo respalda en honorarios, soporte y condiciones.
4. **ADR de `docs/decisiones/`**: deciden lo que las fuentes dejaron «por validar».
5. **`docs/requisitos/base-proyecto.md`**: síntesis de todo lo anterior para trabajar.

Cuidado con la palabra «v2»: en este repositorio designa la **guía técnica del cliente** del 08/10. Los documentos de Luup Lab se citan por su fecha, nunca como «v2» ni «v3».

Usa los identificadores del roadmap cuando existan —`dep-NN`, `dec-NN`, `A01`–`A12`, `M-A01`–`M-A07`—, porque son los que el cliente ve. Los `P0`/`P1`/`P2` de la base agrupan varios de ellos y sirven para priorizar, no para citar.

Si encuentras una regla de las fuentes que la base no refleja, abre un issue de decisión. No la inventes.

## 3. Arquitectura: decisión abierta, no la supongas

La base propone n8n en el VPS Hostinger de Luup Lab y un motor central de cálculo con persistencia en PostgreSQL, separado de los adaptadores de canal, **y lo marca expresamente como propuesta, no como decisión aprobada**. En paralelo, el anexo del cliente describe una plataforma FastAPI con PostgreSQL y un extractor Gemini ya existentes, cuya reutilización está sujeta a autorización de Tu Merch.

**No escribas código que dé por resuelta esa elección.** Hasta que exista un ADR que la cierre:

- La lógica de negocio va en módulos sin dependencias de HTTP, de n8n ni de un proveedor concreto, para que sobreviva a cualquiera de las dos opciones.
- Los proveedores externos van detrás de puertos con una interfaz propia.
- Si una tarea no se puede hacer sin elegir, detente y dilo en el issue.

Lo que sí está decidido y vale en ambas opciones:

- **Todo efecto externo pasa por la cola de operaciones** con clave única por destino, acción y operación, y respeta los modos `off` / `shadow` / `allowlist` / `live` de WF-00. En `shadow` se registra la intención y no se ejecuta nada.
- La cola distingue cuatro estados: intención registrada, ejecución, confirmación y **resultado incierto**. La idempotencia interna evita ejecutar dos veces el mismo evento; no demuestra que un proveedor externo haya recibido una operación tras un timeout. En ese caso se concilia o se revisa, nunca se reenvía a ciegas.
- Cada cotización guarda una **instantánea**: precio tomado de Shopify, versión de la calculadora, disponibilidad consultada, versiones de reglas aplicadas. El documento no es la evidencia; la instantánea sí.
- La recuperación parte del estado persistido, no de la memoria de una ejecución de n8n.

## 4. Reglas de negocio que no se negocian en código

- Precio de venta = precio de Shopify, que ya incluye el markup. **No multiplicar otra vez.**
- Descuento por monto: reproducir la calculadora original cuando llegue, sobre el subtotal de productos antes de IVA, restado solo del componente de producto. Marcación y transporte nunca elevan el tramo. Mientras no llegue, el punto de integración queda definido y los valores de desarrollo se marcan expresamente como pruebas sin validez comercial.
- IVA 19 % después del cálculo. El redondeo por línea o por documento lo aprueba contabilidad y está pendiente.
- Mínimo por variante en el metacampo `custom.cantidad_minima`.
- Vigencia de cinco días hábiles con festivos de Colombia, zona `America/Bogota`. Una cotización vencida no cobra.
- Transporte gratis en Bogotá y Sabana por encima de $2.000.000; otras ciudades a cargo del cliente. La base exacta y los municipios están pendientes.
- Sin stock o mínimo incumplido: no habilitar cobro, no sustituir producto, color ni cantidad sin aceptación, **no reemplazar un dato desconocido por cero ni por un valor inventado**.
- Pago: 100 % sin marcación, 50 % de anticipo en personalizados. Cada confirmación se procesa una sola vez. Un soporte enviado por WhatsApp no equivale a pago confirmado.
- Factura: borrador, verificación del cliente, autorización del asesor, emisión. **Un timeout nunca es autorización para crear otro documento.**
- Marcación (Fase 2): costo × 1,50 cuando la fuente es costo; un precio de venta publicado no recibe segundo markup. Kits y referencias con personalización incluida no reciben cargo adicional.
- La tolerancia de ±10 % que mencionan las fuentes **no es política aprobada para cobrar**.
- La IA extrae campos y señala ambigüedad. No inventa precios, tasas, referencias ni disponibilidad.

## 5. Prohibiciones

1. Escribir en Shopify. Es solo lectura y no existe adaptador de escritura.
2. Datos personales o fiscales en URLs, logs, mensajes de Telegram, commits, títulos de PR o issues, ni en el repositorio: ni teléfonos, ni RUT, ni conversaciones, ni documentos de clientes.
3. Credenciales, enlaces de un solo uso o valores de configuración en el repositorio. Solo `.env.example` sin valores.
4. Reintentar a ciegas un envío de WhatsApp, un cobro, una orden o una factura.
5. Efectos externos fuera de la cola de operaciones, o sin respetar el modo de WF-00.
6. Texto libre por la API de WhatsApp. Solo plantillas aprobadas por Meta.
7. Tocar contactos o negociaciones reales. Solo los tres contactos QA internos ya etiquetados, con negociaciones prefijadas `QA Luup —`. No asumir que se pueden borrar.
8. Tocar contactos de las secuencias `en-secuencia-navidad`, `en-secuencia-normal` o `secuencia-sin-fecha`, ni las exclusiones comerciales. Se revisan justo antes de cada envío, no solo al detectar la solicitud.
9. Crear o renombrar etapas del embudo de Mercately.
10. Tratar la etiqueta `Desactivar MIA` como veto o como permiso: su semántica está sin resolver (P0-07) y la exclusión comercial es cosa distinta de la desactivación de MIA.
11. Enviar a clientes fuera de horario: L–V 08:00–18:00 y sábado 08:00–13:00, `America/Bogota`. Fuera de eso, a la cola.

## 6. Cómo trabajar

- IDs estables: requisitos `RQ`, decisiones `ADR`, workflows `WF`, casos de aceptación `A01`–`A12` y `M-A01`–`M-A07`, pendientes `P0`/`P1`/`P2`. Úsalos; no inventes una nomenclatura paralela.
- **Separa lo propuesto de lo aprobado** en todo lo que escribas. Es la regla editorial de la base y evita que una propuesta se lea después como decisión.
- Trabajo asíncrono: cada tarea lleva ID, resultado esperado, responsable único, estado, dependencia, evidencia y siguiente acción. Al cerrar un bloque, deja qué cambió, cómo se verificó, qué falta y qué dato o decisión se necesita. Mientras no se reparta el trabajo, el responsable de implementación es «por asignar»: no atribuyas especialidades a Alejo ni a David.
- Ramas por cambio y pull request con problema, solución y validación. Un humano revisa cada PR antes de mezclar. Si toca la infraestructura de Tu Merch, además revisa Miguel, **como revisor del cliente, no como desarrollador**.
- Pruebas: toda regla de negocio nueva lleva prueba; los casos de aceptación llevan el nombre del caso. La evidencia de cada ejecución conserva resultado esperado, resultado obtenido, versión y responsable que aprobó.
- Las exportaciones JSON de n8n van en el repositorio y deben coincidir con la versión desplegada.
- Una solicitud de cambio indica impacto en alcance, precio, fechas y aceptación.
- Commits en español, en imperativo, pequeños.

## 7. Personas

- **Luup Lab:** Alejandro Gil Rivera (dirección, interlocución con el cliente, QA y documentación) y David Ramírez González. Ambos confirmados en desarrollo. Juan Felipe Beltrán, pendiente de participación. Reparto de responsabilidades por acordar.
- **Tu Merch:** Brayan Daniel Ortega Bayona (decisiones comerciales y de alcance), Miguel Fabián Tusso (**revisor técnico del cliente; no desarrolla**), la persona comercial (usuaria y validadora de los casos), contabilidad (Siigo, IVA, evento fiscal) y operación (proveedores, tablas de marcación).
