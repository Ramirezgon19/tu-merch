# Instrucciones para el Agente — Cotizador automático · Tu Merch × Luup Lab

> `CLAUDE.md`, `AGENTS.md` y `GEMINI.md` son **tres archivos independientes con el mismo contenido**: cada herramienta lee el suyo —Claude Code el primero, Codex y los agentes que siguen el estándar `AGENTS.md` el segundo, Gemini CLI el tercero— y los tres deben decir exactamente lo mismo. No son enlaces simbólicos ni un solo archivo. Si cambias uno o registras un aprendizaje en uno, replícalo en los otros dos en el mismo commit. `python3 execution/verificar_directivas.py` falla si difieren y `--arreglar` los iguala desde `CLAUDE.md`; córrelo antes de cada PR.

## Aprendizajes del Agente (Mejora Continua)

> **INSTRUCCIÓN CRÍTICA — LEER PRIMERO:** Esta sección es tu memoria persistente de mejora continua. **Con cada ciclo de ejecución** (al completar una tarea, resolver un error, descubrir un patrón, o ajustar un flujo) **y con cada actualización de cualquier Markdown** (directivas, estos tres archivos, READMEs de scripts), **debes agregar aquí un aprendizaje nuevo** si surgió algo no trivial. El objetivo es que este archivo se vuelva más útil y preciso con el tiempo, acumulando conocimiento del proyecto que no se pierde entre sesiones.
>
> **Qué registrar:** restricciones de APIs descubiertas, rate limits reales, patrones que funcionan, errores que se repiten, decisiones de diseño tomadas con el usuario, supuestos que resultaron falsos, atajos útiles, gotchas del entorno.
>
> **Qué NO registrar:** detalles efímeros de una sola tarea, información ya documentada en la directiva correspondiente, cosas triviales derivables del código.
>
> **Formato de cada aprendizaje:**
> ```
> - **YYYY-MM-DD — [Tema corto]:** Descripción del aprendizaje en 1-3 líneas. **Por qué importa:** consecuencia práctica o cómo aplicarlo en el futuro.
> ```
>
> **Higiene:** si un aprendizaje queda obsoleto o se contradice con otro más reciente, actualízalo o elimínalo en vez de acumular ruido. Mantén la lista ordenada por fecha (más recientes arriba). Si superas ~25 entradas, consolida las más antiguas o promuévelas a la directiva que corresponda.

### Registro de aprendizajes

- **2026-10-13 — Fuentes del cliente en Drive vía Composio:** se descartó un repositorio aparte y el VPS de producción; las fuentes viven en una carpeta restringida de Drive y el stack las lee por Composio, con la clave solo en el `.env` del VPS. **Por qué importa:** nunca copies una fuente al repositorio; y Composio es subencargado bajo la Ley 1581, así que no cargues insumos con datos personales hasta que Tu Merch lo apruebe.
- **2026-10-15 — Mercately corta la conexión al User-Agent de Python:** con `Python-urllib/3.x` la API cierra la conexión TLS sin responder (`Connection reset by peer`; curl con ese mismo agente falla igual) y con un User-Agent propio responde normal. **Por qué importa:** todo adaptador o script contra Mercately envía un `User-Agent` explícito; un reset no es caída del servicio ni error de credenciales.
- **2026-10-15 — Contactos QA de Mercately actualizados por Miguel:** la línea de Angie ya no está disponible; quedan Daniela, Miguel y una línea de Luup Lab, las tres con `prueba-luuplab` y `Desactivar MIA`. Miguel pide escribir primero desde la línea QA para abrir la ventana de 24 h antes de cualquier mensaje libre. **Por qué importa:** la guía v2 §1.4 quedó desactualizada; y el mensaje libre dentro de la ventana choca con la prohibición 6, que sigue vigente hasta registrar la decisión.
- **2026-10-15 — Variables vacías del entorno tapan el `.env`:** el shell de Alejo exporta `MERCATELY_QA_TELEFONO` vacía y `os.environ.setdefault` no la reemplazaba. **Por qué importa:** los cargadores de `.env` tratan una variable vacía como no definida.
- **2026-10-15 — Shopify real difiere de la guía v2:** el mínimo `custom.cantidad_minima` está a nivel de **producto** y es texto; hay un segundo mínimo `theme.cus_qty`; parte del catálogo antiguo no tiene `variant.sku`; hay 1.888 productos ACTIVE, no ~1.600. **Por qué importa:** no asumas mínimo por variante ni SKU siempre presente; detalle en el issue #19.
<!-- Agrega nuevas entradas arriba de esta línea. -->
- **2026-10-13 — El repositorio es público:** la base decía «repositorio privado confirmado» y el repositorio `Ramirezgon19/tu-merch` es público; se subieron propuesta, roadmap y guía bajo NDA dando por cierto el documento. **Por qué importa:** la visibilidad se verifica contra GitHub (`gh api … --jq .visibility`), nunca contra lo que diga la documentación; regla 13 de prohibiciones.
- **2026-10-13 — El roadmap manda; las fuentes del cliente complementan:** el paquete fue insumo del roadmap, pero la guía v2 es del 08/10, posterior al roadmap del 01/10, y trae detalle que el roadmap no pudo incluir. **Por qué importa:** no asumas que todo lo del cliente «ya está en el roadmap»; úsalo para el detalle y regístralo si contradice.
- **2026-10-13 — Tres archivos, no uno:** decir que `CLAUDE.md`, `AGENTS.md` y `GEMINI.md` «son el mismo archivo» hizo pensar que eran un solo archivo o enlaces simbólicos. Son tres archivos regulares con contenido idéntico, porque cada herramienta lee un nombre distinto. **Por qué importa:** nunca los conviertas en enlaces simbólicos (Codex y algunos entornos Windows no los siguen) y describe siempre la relación como «independientes e idénticos».
- **2026-10-12 — GraphQL bloqueado en sesiones en la nube:** `gh pr create` y `gh pr view` fallan desde una sesión de Claude en la nube porque usan GraphQL; la API REST (`gh api repos/{owner}/{repo}/pulls`) funciona. En Claude Code o Codex locales, con credenciales propias, `gh pr create` sí funciona. **Por qué importa:** usa `execution/crear_pr.py` o la API REST directa desde la nube; no insistas con el comando de alto nivel.
- **2026-10-12 — El clon de sesión solo sigue `main`:** el refspec del clon que monta una sesión en la nube es `+refs/heads/main:refs/remotes/origin/main`, así que `git status` nunca ve otras ramas remotas aunque el push haya funcionado. **Por qué importa:** la verdad sobre qué hay en GitHub es `git ls-remote origin`, no `git status`; no reintentes un push por lo que diga el estado local.
- **2026-10-12 — Google Drive guarda archivos «solo en la nube»:** un shell que lee un archivo no descargado falla con *Resource deadlock avoided*, y la sincronización de Drive corrompe `.git`. **Por qué importa:** git trabaja en un clon local fuera de Drive; Drive es archivo documental, nunca directorio de trabajo.
- **2026-10-12 — «v2» ya tiene dueño:** en este repositorio «v2» es la guía técnica de integración del cliente del 08/10. Los documentos de Luup Lab se citan por fecha. **Por qué importa:** evita confundir dos documentos de autoridad distinta.
- **2026-10-12 — El roadmap aprobado omite festivos:** declara 12/10, 2/11 y 16/11 y le faltan 8/12 y 25/12. **Por qué importa:** el mismo calendario alimenta la vigencia de cinco días hábiles de una cotización; corregirlo antes de implementar la vigencia.
- **2026-10-12 — macOS trae bash 3.2:** `${var,,}`, `declare -A`, `mapfile` son de bash 4 y fallan en el Mac de Alejo. **Por qué importa:** los scripts del repositorio se escriben para bash 3.2 o en Python.

---

Tú operas dentro de una arquitectura de 3 capas que separa responsabilidades para maximizar la confiabilidad. Los LLMs son probabilísticos, mientras que la mayoría de la lógica de negocio es determinista y requiere consistencia. Este sistema resuelve esa incompatibilidad.

## La Arquitectura de 3 Capas

**Capa 1: Directiva (Qué hacer)**
- Básicamente son SOPs escritos en Markdown, ubicados en `directives/`
- Definen los objetivos, entradas, herramientas/scripts a usar, salidas y casos extremos
- Instrucciones en lenguaje natural, como las que le daría a un empleado de nivel medio

**Capa 2: Orquestación (Toma de decisiones)**
- Esta es tu función. Tu trabajo: enrutamiento inteligente.
- Leer directivas, llamar herramientas de ejecución en el orden correcto, manejar errores, pedir aclaraciones, actualizar directivas con los aprendizajes
- Tú eres el puente entre la intención y la ejecución. Por ejemplo, no intentes armar la evidencia de un caso de aceptación por tu cuenta—lee `directives/evidencia_caso.md`, define entradas/salidas y luego ejecuta `execution/generar_evidencia.py`

**Capa 3: Ejecución (Hacer el trabajo)**
- Scripts de Python deterministas en `execution/`
- Variables de entorno, tokens de API, etc. se almacenan en `.env`
- Manejan llamadas a APIs, procesamiento de datos, operaciones de archivos e interacciones con bases de datos
- Confiables, testeables, rápidos. Use scripts en vez de trabajo manual.

**Por qué funciona esto:** si tú haces todo por tu cuenta, los errores se acumulan. Un 90% de precisión por paso = 59% de éxito en 5 pasos. La solución es empujar la complejidad hacia código determinista. Así tú te concentras solo en la toma de decisiones.

**En este proyecto, el producto no es un script.** El motor de cotización vive en `motor/` y los flujos de n8n en `workflows/`; son el sistema que se entrega al cliente. `execution/` guarda las herramientas con las que el equipo y los agentes operan el proyecto: validar, generar evidencia, cargar issues, respaldar volúmenes, verificar que estos tres archivos sigan iguales. Las reglas de las tres capas aplican a ambos: lógica determinista en código probado, decisiones en el agente, instrucciones en directivas.

## Principios de Operación

**1. Revise primero si existen herramientas**
Antes de escribir un script, revisa `execution/` según tu directiva. Solo crea scripts nuevos si no existe ninguno.

**2. Auto-corrección cuando algo falla**
- Lee el mensaje de error y el stack trace
- Corrige el script y pruébalo de nuevo (a menos que use tokens/créditos de pago—en ese caso consulta primero con el usuario)
- Actualiza la directiva con lo que aprendiste (límites o rate limits de API, tiempos, casos extremos)
- Ejemplo: si llegas al rate limit de una API → investigas la API → encuentras un endpoint batch que soluciona el problema → reescribes el script → pruebas → actualizas la directiva.

**3. Actualice las directivas a medida que aprende**
Las directivas son documentos vivos. Cuando descubras restricciones de API, mejores enfoques, errores comunes o expectativas de tiempo—actualiza la directiva. Pero no crees ni sobreescribas directivas sin preguntar, a menos que se te indique explícitamente. Las directivas son tu conjunto de instrucciones y deben preservarse (y mejorarse con el tiempo, no usarse de manera improvisada y luego descartarse).

## Ciclo de Auto-corrección

Los errores son oportunidades de aprendizaje. Cuando algo falla:
1. Corrija el problema
2. Actualice la herramienta
3. Pruebe la herramienta, asegúrese de que funcione
4. Actualice la directiva con el nuevo flujo
5. El sistema ahora es más robusto

## Organización de Archivos

- `directives/` — SOPs en Markdown (el conjunto de instrucciones). `directives/README.md` es el índice y dice qué directiva gobierna cada entregable del roadmap.
- `execution/` — Scripts deterministas con los que se opera el proyecto.
- `motor/`, `workflows/`, `schemas/`, `tests/` — El producto: motor de cotización, flujos n8n exportados en JSON, contratos de datos y pruebas. Se crean cuando tengan contenido.
- `infra/` — `docker-compose.yml`, `.env.example` y los procedimientos de respaldo, restauración y migración (ADR-002).
- `docs/` — Requisitos, decisiones y operación. `docs/requisitos/base-proyecto.md` es la base del proyecto; `docs/decisiones/` son los ADR.
- `.tmp/` — Todos los archivos intermedios. Nunca se suben al repositorio, siempre se regeneran.
- `.env` — Variables de entorno y claves. Nunca en el repositorio; `infra/.env.example` lleva las claves sin valores.

**Principio clave:** Los archivos intermedios viven en `.tmp/` y pueden borrarse siempre. Cualquier salida del flujo debe ser reproducible ejecutando el flujo de nuevo, nunca editada a mano.

## Al abrir una sesión

1. Lee la sección de aprendizajes de arriba.
2. Lee `docs/requisitos/base-proyecto.md` y `docs/decisiones/` completo.
3. Lee `directives/README.md` y la directiva de lo que vas a hacer. **Nada sin issue:** el criterio de terminado del issue es el contrato, y `directives/trabajar_issue.md` dice cómo tomarlo.
4. Para una regla de negocio, la cadena de autoridad está abajo. No resuelvas por conveniencia una contradicción entre fuentes: eso se registra con `directives/registrar_decision.md`, no se decide en código.

## Autoridad de las fuentes, en orden

1. **Roadmap aprobado del 01/10/2026** (`docs/requisitos/roadmap-aprobado-20261001.md`): **la fuente de la verdad.** Es lo que Tu Merch aprobó: alcance, entregables y criterios por etapa K/D1/D2/D3, los 19 casos de aceptación, las dependencias `dep-01`–`dep-15`, las decisiones `dec-01`–`dec-10` y las exclusiones. Gana ante cualquier contradicción. La propuesta del mismo día lo respalda en honorarios y condiciones.
2. **ADR de `docs/decisiones/`**: deciden lo que el roadmap dejó abierto. ADR-001 trata el cronograma; ADR-002, el despliegue; ADR-003, el almacenamiento de fuentes del cliente en Drive vía Composio.
3. **Fuentes complementarias del cliente**: el paquete de estimación v1 (funcional del 19/09 y anexo técnico del 24/09) y la guía técnica de integración v2 del 08/10. Sirven para el **detalle que el roadmap no cubre** —contratos de API, metacampos, convivencia con MIA, contactos QA— y nada más. El paquete fue insumo del roadmap; la guía v2 es posterior a él y por eso trae información nueva que el roadmap no pudo incluir. Si cualquiera de las dos contradice el roadmap, **no se aplica**: se registra con `directives/registrar_decision.md`. Si amplía el alcance, es una solicitud de cambio, no código.
4. **Información nueva del cliente durante la ejecución** —documentos, correos, mensajes del grupo de WhatsApp— entra solo por `directives/incorporar_fuente.md`, que decide dónde se organiza y qué relevancia tiene. Hasta pasar por ahí, no es fuente.
5. **`docs/requisitos/base-proyecto.md`**: síntesis de todo lo anterior para trabajar. Si contradice al roadmap, gana el roadmap y la base se corrige.

«v2» designa la guía técnica del cliente. Los documentos de Luup Lab se citan por fecha. Usa los identificadores del roadmap —`dep-NN`, `dec-NN`, `A01`–`A12`, `M-A01`–`M-A07`— porque son los que el cliente ve; los `P0`/`P1`/`P2` de la base priorizan, no citan.

## Arquitectura decidida (ADR-002)

Contenedores Docker sobre un VPS de Luup Lab, aislados del resto del VPS, con n8n orquestando y un motor propio con PostgreSQL. El conjunto **migrará a otro VPS**, así que desde el primer commit: todo declarado en `infra/docker-compose.yml`, nada en el host, estado solo en volúmenes nombrados, secretos solo en `.env`, imágenes fijadas por versión, respaldo y restauración como scripts probados. La plataforma FastAPI de Tu Merch no es el runtime.

Invariantes que valen en todo el sistema:
- **Todo efecto externo pasa por la cola de operaciones**, con clave única por destino, acción y operación, y respeta los modos `off` / `shadow` / `allowlist` / `live` de WF-00. En `shadow` se registra la intención y no se ejecuta nada.
- La cola distingue intención registrada, ejecución, confirmación y **resultado incierto**. La idempotencia interna no demuestra que un proveedor recibió una operación tras un timeout: se concilia o se revisa, nunca se reenvía a ciegas.
- Cada cotización guarda una **instantánea**: precio tomado de Shopify, versión de la calculadora, disponibilidad consultada, versiones de reglas. El documento no es la evidencia; la instantánea sí.
- La lógica de negocio vive en `motor/` sin dependencias de HTTP, de n8n ni de un proveedor; los proveedores van detrás de puertos. La recuperación parte del estado persistido, no de la memoria de una ejecución de n8n.

## Reglas de negocio que no se negocian en código

- Precio de venta = precio de Shopify, que ya incluye el markup. **No multiplicar otra vez.**
- Descuento por monto: reproducir la calculadora original cuando llegue, sobre el subtotal de productos antes de IVA, restado solo del componente de producto. Marcación y transporte nunca elevan el tramo. Mientras no llegue, el punto de integración queda definido y los valores de desarrollo se marcan como pruebas sin validez comercial.
- IVA 19 % después del cálculo. El redondeo lo aprueba contabilidad (`dec-01`) y está pendiente.
- Mínimo por variante en el metacampo `custom.cantidad_minima`.
- Vigencia de cinco días hábiles con festivos de Colombia, zona `America/Bogota`. Una cotización vencida no cobra.
- Transporte gratis en Bogotá y Sabana por encima de $2.000.000; otras ciudades a cargo del cliente. Base exacta y municipios pendientes (`dec-02`).
- Sin stock o mínimo incumplido: no habilitar cobro, no sustituir producto, color ni cantidad sin aceptación, **no reemplazar un dato desconocido por cero ni por un valor inventado**.
- Pago: 100 % sin marcación, 50 % de anticipo en personalizados. Cada confirmación se procesa una sola vez. Un soporte por WhatsApp no es pago confirmado.
- Factura: borrador, verificación del cliente, autorización del asesor, emisión. **Un timeout nunca autoriza crear otro documento.**
- Marcación (Fase 2): costo × 1,50 cuando la fuente es costo; un precio publicado no recibe segundo markup. Personalización incluida no se cobra dos veces.
- La tolerancia de ±10 % de las fuentes **no es política aprobada para cobrar**.
- La IA extrae campos y señala ambigüedad. No inventa precios, tasas, referencias ni disponibilidad.

## Prohibiciones

1. Escribir en Shopify. Es solo lectura y no existe adaptador de escritura.
2. Datos personales o fiscales en URLs, logs, Telegram, commits, PRs, issues ni en el repositorio: ni teléfonos, ni RUT, ni conversaciones, ni documentos de clientes.
3. Credenciales, enlaces de un solo uso o valores de configuración en el repositorio, en imágenes Docker o en `docker-compose.yml`. Solo `infra/.env.example` sin valores.
4. Reintentar a ciegas un envío de WhatsApp, un cobro, una orden o una factura.
5. Efectos externos fuera de la cola de operaciones o sin respetar el modo de WF-00.
6. Texto libre por la API de WhatsApp. Solo plantillas aprobadas por Meta.
7. Tocar contactos o negociaciones reales. Solo los contactos QA etiquetados `prueba-luuplab` —desde el 15/10/2026 Daniela, Miguel y la línea de Luup Lab; la de Angie ya no está disponible—, con negociaciones prefijadas `QA Luup —` que se borran al terminar. Verifica las etiquetas del contacto por API antes de escribir.
8. Tocar contactos de las secuencias `en-secuencia-navidad`, `en-secuencia-normal` o `secuencia-sin-fecha`, ni las exclusiones comerciales. Se revisan justo antes de cada envío.
9. Crear o renombrar etapas del embudo de Mercately.
10. Tratar la etiqueta `Desactivar MIA` como veto o como permiso: su semántica está sin resolver (P0-07).
11. Enviar a clientes fuera de horario: L–V 08:00–18:00 y sábado 08:00–13:00, `America/Bogota`. Fuera de eso, a la cola.
12. Dependencias en el host del VPS, rutas absolutas del VPS o imágenes `latest`. Rompe la migración (ADR-002).
13. **Subir al repositorio cualquier documento del cliente, su transcripción, precios, honorarios o datos de personas de Tu Merch mientras el repositorio sea público.** Verifica la visibilidad con `gh api repos/Ramirezgon19/tu-merch --jq .visibility` antes de subir algo que venga del cliente; no confíes en lo que diga un documento. El material del cliente vive en la carpeta de Drive del proyecto y se accede por Composio (ADR-003); al repositorio solo llegan citas por fecha, remitente y tipo.

## Cómo trabajar

- IDs estables: `RQ`, `ADR`, `WF`, `A01`–`A12`, `M-A01`–`M-A07`, `P0`/`P1`/`P2`, `dep-NN`, `dec-NN`. No inventes nomenclatura paralela.
- **Separa lo propuesto de lo aprobado** en todo lo que escribas.
- Trabajo asíncrono: cada tarea lleva ID, resultado esperado, responsable único, estado, dependencia, evidencia y siguiente acción. Al cerrar un bloque: qué cambió, cómo se verificó, qué falta, qué dato o decisión se necesita. Mientras no se reparta el trabajo, el responsable es «por asignar».
- Rama por cambio, un PR por issue, con problema, solución y validación. Un humano revisa antes de mezclar. Si toca infraestructura del cliente, además Miguel, como revisor del cliente.
- Toda regla de negocio nueva lleva prueba; los casos de aceptación llevan el nombre del caso. La evidencia conserva resultado esperado, obtenido, versión y quién aprobó.
- Commits en español, en imperativo, pequeños. Antes de cada PR: `python3 execution/verificar_directivas.py`.

## Personas

- **Luup Lab:** Alejandro Gil Rivera (dirección, interlocución con el cliente, QA y documentación) y David Ramírez González. Ambos en desarrollo. Juan Felipe Beltrán, pendiente. Reparto de responsabilidades por acordar.
- **Tu Merch:** Brayan Daniel Ortega Bayona (decisiones comerciales y de alcance), Miguel Fabián Tusso (revisor técnico del cliente; no desarrolla), la persona comercial (usuaria y validadora), contabilidad (Siigo, IVA, evento fiscal), operación (proveedores, tablas de marcación).

## Resumen

Tú estás entre la intención humana (directivas) y la ejecución determinista (scripts de Python). Lee instrucciones, toma decisiones, llama herramientas, maneja errores y mejora el sistema continuamente.

Se pragmático. Se confiable. Auto-corríjete.
