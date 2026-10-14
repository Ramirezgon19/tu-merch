## Issue
Closes #

## Qué cambia
<!-- 3–5 líneas. Qué se construyó y por qué así. -->

## Evidencia del criterio de aceptación
<!-- Enlace a la prueba automática o a docs/evidencia/…; salida de pytest; captura anonimizada si aplica. -->

## Lista de verificación
- [ ] Ninguna escritura en Shopify
- [ ] Ningún dato personal o fiscal en logs, URLs ni en este PR
- [ ] Efectos externos pasan por la bandeja de salida con Idempotency-Key
- [ ] Funciona en modo `shadow` sin efectos externos (si aplica)
- [ ] Reintentos: nunca a ciegas en WhatsApp, pagos, pedidos ni facturas
- [ ] Workflows n8n modificados exportados como JSON en `n8n/`
- [ ] Documentación tocada si cambió una regla, un mapeo o un procedimiento
- [ ] Generado o asistido por agente de código: revisado línea por línea por un humano del frente

## Revisor
<!-- Owner del frente. Si toca infraestructura de TuMerch, añadir a Miguel. -->
