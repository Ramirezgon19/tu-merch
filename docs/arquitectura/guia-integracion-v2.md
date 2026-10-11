> Copia de trabajo revisada el 11/10/2026. Fuente: [guía v2 en Drive](https://drive.google.com/file/d/1bZyWxo16AP3AjY5pSreEhEDZ3VwEQrZK/view). Se omiten los teléfonos internos de prueba. No contiene credenciales ni enlaces de secretos. Las fechas del documento fuente son históricas; consultar la planificación vigente en la [base del proyecto](../requisitos/base-proyecto.md).

# Tu merch — Cotizador automático: guía técnica de integración v2

Fecha: 2026-10-08 (v2: contactos de prueba con números y acceso a Shopify por Dev Dashboard; reemplaza la v1 del 07/10) · Para: equipo Luup Lab · De: tecnología Tu merch (Miguel Tusso)
Complementa el «Paquete de estimación v1» y el anexo técnico ya compartidos. No contiene credenciales: los secretos llegan por canal seguro aparte.

## 0. Reglas de convivencia (leer primero)

1. **Nada a clientes reales** hasta la aceptación de cada despliegue. Pruebas solo con los contactos de prueba autorizados.
2. **Shopify es solo lectura.** No modificar productos, variantes, precios, inventario, estados (ACTIVE/DRAFT) ni metacampos. El inventario lo escribe un solo proceso nuestro (Agente Shopify).
3. **Mercately: escribir solo sobre contactos y negociaciones de prueba.** La api-key es única para toda la cuenta y permite escribir; cualquier escritura sobre negociaciones reales la detectan nuestros vigías y detiene la prueba.
4. **No contactar a nadie con etiqueta `en-secuencia-navidad`, `en-secuencia-normal` ni `secuencia-sin-fecha`**: esos leads están en un piloto de secuencias automáticas activo desde el 07/10/2026 y recibirían doble mensaje.
5. **Envíos a clientes solo en horario hábil** (L–V 08:00–18:00, sáb 08:00–13:00 Bogotá). De noche, el mensaje espera.
6. **MIA (agente IA «Danna») responde a todo saliente nuestro** por la regla «Activar MIA en primer mensaje de salida» (encendida). Si el cotizador toma una negociación, apáguenla en ese contacto con la etiqueta `Desactivar MIA` (ya está en las exclusiones del agente).
7. Contacto técnico único: Miguel. Nada de secretos por WhatsApp o correo en claro.

## 1. Mercately

### 1.1 Embudo «1. Proceso de venta» (nombres exactos)
Etapas en orden, con su automatización nativa (solo mueven la tarjeta, nunca envían mensajes):

| Etapa | Automatización nativa |
|---|---|
| Nuevo Cliente | ninguna |
| Cantidad, Logo y Producto ✅ | ninguna |
| Propuesta Enviada | a los 2 días → Primer Seguimiento |
| Proceso de Pago - OC | ninguna |
| Primer Seguimiento | a los 3 días → Llamada + Correo |
| Llamada + Correo | a los 2 días → Segundo Seguimiento |
| Segundo Seguimiento | a los 2 días → Llamada + whatsapp Tercer Seguimiento |
| Llamada + whatsapp Tercer Seguimiento | a los 7 días → Mensaje Final |
| Mensaje Final | ninguna |
| Cerrado y ganado | al entrar → embudo 2, etapa «Gestión de Proveedores» |
| Enfrío | ninguna |
| Cerrado y perdido | ninguna |

Otros embudos: «2. Tramitación de pedidos» (Gestión de Proveedores → Mock up Digital → Orden de Produccion Aprobada → Muestra Inicial → Producción → Fotos y Videos → Pago Recibido → Factura Electrónica Enviada …) y «3. Postventa y testimonio».

Propuesta de encaje (a confirmar en el kickoff): el cotizador se dispara en «Cantidad, Logo y Producto ✅» y, al enviar el PDF, mueve la tarjeta a «Propuesta Enviada» (desde ahí corren los seguimientos nativos). Brayan es el dueño de las etapas: no crear ni renombrar etapas sin su confirmación.

### 1.2 Etiquetas relevantes
- Exclusión: `no-contactar`, `no-es-lead`, `base-anterior`, `Desactivar MIA`.
- Piloto de secuencias (no tocar): `en-secuencia-navidad`, `en-secuencia-normal`, `secuencia-sin-fecha`, `sin-respuesta`, `llamada-sin-respuest`, `seguimiento-auto`, `aun-no-es-momento`.
- Origen: `lead-meta1`, `lead-navidad-meta`, `lead-meta-ads`, `FACEBOOK ANUNCIOS`, `Página Web`.
- Propuesta para el cotizador: `prueba-luuplab` en los contactos de prueba, y una etiqueta propia por estado del cotizador (p. ej. `cotizador:en-proceso`, `cotizador:enviada`) para no colisionar con las anteriores.

### 1.3 Particularidades de la API (aprendidas en producción, septiembre–octubre 2026)
- `PUT /customers/:phone` con `tags` **solo añade**; para quitar una etiqueta hay que enviarla con `value: false`. Enviar siempre `customer.first_name` para no borrarlo. Las etiquetas van como objetos `{"name": ..., "value": true}` en `tags` al nivel raíz del cuerpo, fuera de `customer` (dentro de `customer` la API responde 200 y no aplica nada).
- `PUT /deals/:id` exige `deal.customer_id` con el id de contacto **tal como lo devuelve `GET /customers/:phone`** (texto). Con el id numérico de `deal.customer.id` responde 500.
- `GET /deals/:id` devuelve la etapa con adorno («Cantidad, Logo y Producto  ✅»): comparar normalizando. En listados, `customer.id` es numérico y el id real del contacto va en `web_id`.
- Las plantillas con imagen exigen `media_url` en cada envío; la API de plantillas no expone la imagen cargada. Alojen la imagen en una URL pública estable.
- El envío de plantilla no devuelve identificador del mensaje y la conversación no trae `sent_by_mia`: por API no se distingue un saliente de MIA de uno humano. Usen `direction`, `created_time` (ISO UTC), `status` y una ventana de gracia tras el propio envío.
- Campos útiles de mensajes: `content_type`, `content_media_type`, `content_media_url`, `filename`, `content_media_caption`, `direction`, `created_time`, `status`.
- El detalle de una negociación no trae productos, notas ni campos personalizados: producto y cantidad se infieren de la conversación.
- Lectura de conversaciones: `GET /customers/:phone/whatsapp_conversations?page=1&results_per_page=100`.
- Mercately crea el contacto si se le envía una plantilla a un número que no existe; aun así, creen el contacto antes (POST) con nombre y etiquetas.

### 1.4 Contactos de prueba
Definidos el 08/10/2026: tres líneas internas de Tu merch.

| Persona | WhatsApp |
|---|---|
| Angie (comercial) | Consultar en el original de Drive |
| Daniela (marketing) | Consultar en el original de Drive |
| Miguel (tecnología) | Consultar en el original de Drive |

Ya llevan `Desactivar MIA` y `prueba-luuplab`. Angie y Daniela también reciben los avisos internos del equipo: los mensajes de prueba deben identificarse como prueba para no confundirse con clientes. Toda negociación de prueba se nombra con prefijo «QA Luup —» y se borra al terminar (`DELETE /deals/:id`).

## 2. Shopify

- Acceso: app «Luup Lab cotizador (lectura)» creada en el Dev Dashboard de Shopify el 08/10/2026, con permisos `read_products`, `read_inventory`, `read_locations` y Admin API 2026-10. Las credenciales (Client ID y Client secret) ya se enviaron por enlace de un solo uso; el token se obtiene con el flujo client credentials. Tienda: `tumerchco.myshopify.com`. Se revoca desinstalando la app al cierre.
- Ubicación de inventario única: `108638666884`.
- Catálogo: ~1.600 productos ACTIVE y ~120 DRAFT. Cada variante lleva el **SKU del proveedor** (PromoOpción, CDO, Marpico) en `variant.sku`; el precio de venta ya incluye el margen (no volver a aplicar el 40 %).
- Política de inventario `deny` en variantes ACTIVE: con inventario 0 no se vende. El inventario lo sincroniza nuestro agente cada 20 min con los proveedores; puede tener desfase de horas al cierre del día.
- Mínimos de compra (MOQ): están en reglas de Shopify y en la calculadora comercial; validen contra la calculadora que entrega Brayan (caso A03).
- Límite de tasa: 2 solicitudes/s en REST; reintentar en 429 respetando `Retry-After`.
- No usar `write_*`. No cambiar `status`. No crear variantes.

## 3. Formato de la cotización
Referencia: PDF real «Cotización UNIQUE VINEYARD II» (Nº 4002) e imágenes 01–06 en la carpeta compartida. Reglas duras: bloque izquierdo = datos del cliente (variables), bloque derecho = datos de Tu merch (fijos: NIT 901938983-1, hola@tumerch.co, Avenida 1ro de Mayo # 24D-27); nunca cruzarlos. Tabla Producto | Cantidad | Precio | Total; Subtotal sin IVA, IVA 19 %, Total. Firma «Gerente de ventas». Páginas fijas de responsabilidad social y términos.

## 4. Lo que Tu merch ya automatiza (para no duplicar ni chocar)
- Leads de Meta (3 campañas) → aviso al equipo + primer toque por plantilla + escritura en CRM (n8n).
- Piloto de secuencias de Navidad (166): ingreso automático de leads de Navidad al embudo con etiqueta `en-secuencia-navidad`, 3 impactos por plantilla, cierre a «Enfrío» si no responde.
- Agente Shopify: inventario y fichas desde proveedores.
- Kesher: canal de WhatsApp para pedidos de kits con operadores.
- Vigías: outbox de mensajes, monitor de stock, auditoría de facturas. Cualquier envío masivo o escritura inesperada genera alerta.

## 5. Entrega y transferencia al cierre
- Repositorio, n8n y motor en infraestructura de Luup Lab durante la construcción. Al cierre: repositorio completo transferido al GitHub de Tu merch, workflows exportados en JSON, variables de entorno documentadas sin valores, runbook de despliegue y rollback.
- Antes de publicar algo en el n8n de Tu merch pasa por revisión nuestra (pruebas, guarda de deriva repo↔n8n, respaldo).
- Al cierre se rota la api-key de Mercately de forma coordinada (nuestros flujos también la usan), se desinstala la app de Shopify y se retiran las etiquetas de los contactos de prueba.

## 6. Pendientes de terceros (fuera de tecnología)
| Qué | Responsable | Fecha de Luup Lab |
|---|---|---|
| Calculadora de descuentos .xlsx | Brayan | 7 oct |
| Cinco cotizaciones reales recientes | Brayan | 7 oct |
| Asesora comercial 2 h/día para aceptación | Brayan | 13–14 oct |
| Credenciales API Siigo y ambiente de pruebas | Contabilidad | 15 oct |
| Procedimiento de facturación real | Contabilidad | 21 oct |
| Lista de proveedores, WhatsApp y formato de pedido | Operaciones | antes de D3 |
| Llaves Bold y ambiente de pruebas (opcional) | Brayan/contabilidad | 15 oct |
