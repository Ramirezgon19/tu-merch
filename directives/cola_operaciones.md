# Directiva: cola de operaciones y modos de salida (WF-00)

**Objetivo.** Que ningún efecto externo ocurra fuera de control, dos veces, o a ciegas. Es el invariante central del sistema y el que el cliente exige en el anexo §4.4 y §4.5.

**Aplica a** todo lo que sale del sistema: WhatsApp por Mercately, movimientos de etapa en el CRM, Siigo, Bold, Drive, Telegram, órdenes al proveedor.

**Reglas.**
1. Toda operación externa se registra primero como **intención** en la cola, con clave única por destino, acción y operación. Nunca se llama a un proveedor desde un caso de uso.
2. El **modo** global (`MODO_OPERACION` en `.env`) y el modo por destino deciden si se ejecuta: `off` no registra ni ejecuta; `shadow` registra la intención y no ejecuta nada; `allowlist` ejecuta solo hacia entidades autorizadas (contactos QA, clientes del piloto); `live` ejecuta. Toda prueba del motor pasa en `shadow` sin ningún efecto externo, y existe una prueba que lo demuestra.
3. Cuatro estados, no dos: intención registrada, en ejecución, confirmada, **resultado incierto**. Un timeout o una respuesta ambigua del proveedor dejan la operación en incierto. Incierto se concilia (consultando el estado al proveedor) o se revisa a mano. **Nunca se reenvía.**
4. La idempotencia interna evita ejecutar dos veces el mismo evento. No demuestra que el proveedor recibió algo. No la uses como argumento para reintentar.
5. Un evento repetido de entrada (webhook duplicado, doble confirmación) produce una sola operación. Caso A11.
6. Horario: los envíos a clientes solo L–V 08:00–18:00 y sábado 08:00–13:00, `America/Bogota`. Fuera de horario, la operación queda en cola.
7. Justo antes de ejecutar un envío, se revalida exclusión comercial, secuencias activas y etiqueta de prueba del contacto, no solo al detectarlo.
8. La recuperación tras un fallo parte del estado persistido de la cola, nunca de la memoria de una ejecución de n8n.

**Casos extremos.** Reenvío de confirmación de pago: no duplica pedido ni factura. Error de factura: conservar, notificar, reintentar controladamente; nunca generar otro documento sin verificar el anterior. Proveedor que no confirma: alerta, no reenvío.
