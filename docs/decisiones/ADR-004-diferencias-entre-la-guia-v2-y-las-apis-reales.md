# ADR-004 · Diferencias entre la guía v2 y lo que exponen las APIs reales

**Estado:** propuesta. No es decisión aprobada. Propone Alejo el 15/10/2026; decide Miguel en lo técnico y Brayan en lo comercial (punto 2).
**Fecha:** 15 de octubre de 2026 · **Propone:** Alejo · **Decide:** Miguel (puntos 1, 3, 4) y Brayan (punto 2)
**Cierra:** las contradicciones que exige registrar el criterio del issue #19
**Fuentes:** sondeo de solo lectura del 14–15/10 con `execution/sondear_apis.py` (issue #19); guía v2 §1.3, §1.4 y §2; mensaje de Miguel del 15/10 con las condiciones de prueba (en Drive, ADR-003); prohibiciones 6 y 7 de `CLAUDE.md`

## Contexto

El sondeo leyó Shopify (producción, solo lectura) y Mercately (solo el contacto QA de Luup Lab). Se registró la forma de las respuestas, nunca sus valores. Cuatro hallazgos contradicen la guía v2 o las reglas del repositorio y no se pueden resolver en código por conveniencia.

## Hallazgos y decisión propuesta

**1. El mínimo de compra está en el producto, no en la variante.** La guía y `CLAUDE.md` dicen «mínimo por variante en `custom.cantidad_minima`». En la muestra, el metacampo aparece en 50 de 50 productos y en 0 de 206 variantes, y su tipo es `single_line_text_field`, no entero.
*Propuesta:* el motor lee el mínimo del producto y lo aplica a la suma de las variantes de la línea o a cada variante, según confirme Miguel. Convertir texto a entero; si no es un entero, bloquear la línea con `pendiente_datos`, nunca tratarlo como cero.

**2. Hay dos campos de mínimo.** `theme.cus_qty` (entero) coincide con `custom.cantidad_minima` en los 50 productos muestreados.
*Propuesta:* `custom.cantidad_minima` es la fuente, porque es la que cita la guía; si los dos difieren en un producto, se bloquea la línea y se avisa. Brayan confirma, porque el mínimo también vive en la calculadora (caso A03).

**3. No todas las variantes tienen SKU del proveedor.** La guía dice que cada variante lleva el SKU en `variant.sku`. Los 100 productos actualizados más recientemente lo tienen; los 50 más antiguos no lo tienen en `sku`, `barcode` ni `inventoryItem.sku`. Los formatos varían por proveedor, con espacios y guiones.
*Propuesta:* WF-03 cotiza un producto sin SKU, pero WF-09 no puede ordenarlo al proveedor: la orden queda bloqueada y va a revisión humana. Normalizar el SKU solo para comparar, enviarlo tal cual. Pedir a Miguel si el agente de Shopify va a completar los SKU faltantes.

**4. Mensajes libres dentro de la ventana de 24 h.** Miguel autorizó el 15/10, para pruebas, mensajes libres después de que la línea QA escriba primero a la línea de Tu Merch. La prohibición 6 dice «solo plantillas aprobadas por Meta».
*Propuesta:* la prohibición 6 se mantiene para clientes. Para los contactos QA se permite texto libre solo dentro de la ventana abierta por el propio contacto, identificado como prueba. Hasta que Miguel confirme esta lectura por escrito, solo plantillas.
*Actualización 15/10/2026:* la cuestión queda resuelta por la plataforma. La conexión de Tu Merch es API oficial vía Gupshup, y la API pública de Mercately solo ofrece texto libre (`/whatsapp/send_message`) para conexiones por QR. Con la ventana abierta por la línea QA, un intento único respondió 500 y no salió nada. El cotizador solo envía plantillas; el texto libre queda para personas desde el inbox. Detalle en `docs/operacion/pruebas-mercately.md`.
*Confirmado por Miguel el 15/10/2026:* en la API oficial los salientes automáticos solo van por plantilla aprobada; Tu Merch ya reprodujo el mismo 500 en agosto. No se abre usuario de Mercately para Luup Lab; las respuestas del vendedor en pruebas se simulan con la plantilla `cotizador_respuesta_solicitud`. **Punto 4 cerrado.**

## Otros hallazgos que complementan sin contradecir

- El token de Shopify solo tiene `read_inventory`, `read_locations` y `read_products`: sin permisos de escritura.
- 1.888 productos ACTIVE, no ~1.600; hasta 52 variantes por producto; opciones `Color` y `Cantidad de Colores`. Esta última parece marcación codificada como variante y debe revisarse antes de la Fase 2 para no cobrar marcación dos veces.
- Mercately corta la conexión TLS con el User-Agent por defecto de Python; los adaptadores envían uno propio.
- El GET de contacto devuelve etiquetas como `{tag, web_id}`; la guía documenta que el PUT las espera como `{name, value}` en la raíz.
- Contactos QA vigentes desde el 15/10: Daniela, Miguel y la línea de Luup Lab. La de Angie ya no está disponible (prohibición 7 actualizada).

## Consecuencias

- El issue #12 deja de decir «mínimo por variante» cuando se apruebe el punto 1.
- La copia del catálogo para pruebas (comentario en #15) debe incluir productos sin SKU y con los dos campos de mínimo.

## Pendiente para cerrar este ADR

Confirmación escrita de Miguel sobre los puntos 1, 3 y 4, y de Brayan sobre el punto 2.
