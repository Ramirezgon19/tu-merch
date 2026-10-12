# AGENTS.md — Cotizador automático · Tu Merch × Luup Lab

Instrucciones para agentes de código. Son las mismas reglas de `CLAUDE.md`; léelo completo antes de la primera tarea. Esto resume lo operativo.

## Antes de empezar

1. Lee `docs/requisitos/base-proyecto.md` y todo `docs/decisiones/`.
2. Lee el issue asignado. **El criterio de terminado es el contrato.** Si falta información, coméntalo en el issue y detente; no rellenes con supuestos.
3. Lee las secciones 3, 4 y 5 de `CLAUDE.md`: arquitectura abierta, reglas de negocio y prohibiciones.
4. Si el issue depende de un pendiente P0/P1/P2 sin resolver, detente y avísalo.

## La arquitectura no está decidida

La base propone n8n en el VPS de Luup Lab con motor propio, y lo marca como propuesta. La reutilización de la plataforma FastAPI existente de Tu Merch está sujeta a autorización. **No escribas código que dé por resuelta esa elección:** lógica de negocio en módulos sin dependencias de HTTP, de n8n ni de un proveedor concreto, y proveedores detrás de puertos. Si la tarea no se puede hacer sin elegir, dilo en el issue.

## Reglas duras (fallar cualquiera invalida el PR)

- Shopify es solo lectura. No existe adaptador de escritura y no debes crearlo.
- Ningún dato personal o fiscal en logs, URLs, mensajes, commits, PRs, issues ni archivos del repositorio.
- Ninguna credencial ni valor de configuración en el repositorio. Solo `.env.example` sin valores.
- Todo efecto externo pasa por la cola de operaciones, con clave única por destino, acción y operación, y respeta el modo de WF-00. En `shadow` no sale nada.
- La cola distingue intención, ejecución, confirmación y **resultado incierto**. Ante respuesta incierta de un proveedor: conciliar o revisar, nunca reenviar.
- Nunca reintentes a ciegas un envío de WhatsApp, un cobro, una orden o una factura. Un timeout no autoriza crear otro documento.
- Solo plantillas aprobadas por Meta para WhatsApp saliente.
- Solo los contactos QA internos etiquetados, con negociaciones prefijadas `QA Luup —`. Nunca contactos o negociaciones reales.
- No crear ni renombrar etapas del embudo.
- No reemplazar un dato desconocido por cero ni por un valor inventado. No aplicar un segundo markup al precio de Shopify.

## Cómo entregar

- Rama por cambio; un PR por issue, con problema, solución y validación.
- Pruebas en verde. Regla de negocio nueva → prueba unitaria. Caso de aceptación → prueba con el nombre del caso.
- Evidencia con resultado esperado, resultado obtenido, versión y responsable que aprobó, sin datos sensibles.
- Workflows n8n tocados → exportados como JSON, coincidiendo con la versión desplegada.
- IDs estables: `RQ`, `ADR`, `WF`, `A01`–`A12`, `M-A01`–`M-A07`, `P0`/`P1`/`P2`. No inventes nomenclatura paralela.
- Separa lo propuesto de lo aprobado en lo que escribas.
- Completa la lista de verificación del `PULL_REQUEST_TEMPLATE.md`. Un humano revisa línea por línea antes de mezclar.

## Ante una duda de negocio

No la resuelvas en código. Abre un issue de decisión, cita la sección de la fuente y deja la tarea bloqueada hasta que se registre la decisión como ADR.
