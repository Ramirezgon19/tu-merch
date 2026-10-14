# ADR-003 · Dónde se almacenan las fuentes y los insumos del cliente

**Estado:** decidido por Alejo el 13/10/2026 en la pregunta 2 (almacenamiento): Drive a través de Composio, conectado al contenedor. La pregunta 1 (visibilidad del repositorio) sigue pendiente de David. Requiere confirmación de Miguel sobre el NDA.
**Fecha:** 13 de octubre de 2026 · **Propone:** Alejo · **Decide:** Alejo y David · **Consulta:** Miguel
**Relacionado:** ADR-002 (despliegue); `directives/incorporar_fuente.md`; prohibición 13 de `CLAUDE.md`

## Contexto

El 13/10 se verificó contra GitHub que **`Ramirezgon19/tu-merch` es público**, aunque la base lo daba por privado. En `main` hay hoy material bajo NDA: el roadmap aprobado con su HTML, la propuesta con honorarios, la copia de la guía técnica v2, enlaces a las carpetas de Drive del cliente y nombres de personas de Tu Merch. Además, todo el repositorio —`CLAUDE.md`, la base, los ADR— describe procesos internos del cliente que el NDA cubre aunque no sean documentos suyos.

Por eso hay dos preguntas distintas, y la segunda depende de la primera:

1. ¿El repositorio del proyecto debe ser público?
2. ¿Dónde viven los documentos y los insumos que entrega el cliente?

## Pregunta 1 · Visibilidad del repositorio

**Propuesta: hacerlo privado ya.** Un repositorio público es incompatible con el NDA aunque se saquen los documentos del cliente, porque las reglas de negocio, los nombres de etapas del CRM y la arquitectura del sistema son información del cliente. Un plan gratuito de GitHub permite repositorios privados con colaboradores ilimitados, así que no hay costo. Solo el dueño o un administrador puede cambiarlo, en Settings → General → Danger Zone → Change visibility.

Hacerlo privado detiene la exposición **desde ese momento**. Lo que ya estuvo público pudo ser copiado; para retirarlo también del historial habría que reescribir `main`, lo que obliga a todos a volver a clonar. Se decide aparte, después de evaluar si hubo accesos.

## Pregunta 2 · Almacenamiento de fuentes e insumos

Requisitos: que los agentes (Claude Code, Codex, Gemini, sesiones en la nube) puedan leer las fuentes; que haya versiones; que el acceso sea por persona y revocable; que no aumente el daño si se compromete producción; y que no sume intermediarios que procesen datos del cliente.

| Opción | Lectura por agentes | Riesgo principal |
|---|---|---|
| **A. Repositorio del proyecto, una vez privado** | Directa, con git | Mezcla código y documentos del cliente en el mismo lugar; aceptable si el repo es privado y el NDA lo permite |
| **B. Repositorio privado aparte solo para fuentes** (`tu-merch-fuentes`) | Directa, con git; se clona al lado | Un segundo repo que mantener; separa permisos: se puede dar acceso al código sin dar acceso a los documentos |
| **C. Drive con el conector de Google** | Por el conector de Drive de cada herramienta; Codex y Gemini necesitan configurar el suyo | Drive ya fue fuente de errores de sincronización; versiones menos explícitas que git |
| **D. Drive a través de Composio** | Por la integración de Composio | Agrega un tercero que procesa documentos bajo NDA y datos personales; habría que declararlo al cliente (Ley 1581 de 2012) |
| **E. Volumen restringido en el VPS** | Solo con SSH al servidor de producción | Amplía el acceso a producción para leer documentos; si se compromete n8n, se compromete todo |

**Decisión (Alejo, 13/10/2026): opción D, Drive a través de Composio, conectado al stack del contenedor.** Se descarta B porque no se quiere mantener un segundo repositorio, y E porque mete los documentos en el servidor de producción.

Cómo se implementa:

- **Drive es el almacén** de originales, transcripciones e insumos del cliente, en una carpeta del proyecto de acceso restringido. El repositorio no guarda nada de eso.
- **Composio es el único puente**, configurado en el stack de ADR-002: la clave de Composio vive solo en el `.env` del VPS (`COMPOSIO_API_KEY`), nunca en el repositorio ni en imágenes. La conexión con Google se autoriza contra **esa carpeta**, no contra todo el Drive de quien la autoriza, y con permisos de **solo lectura** salvo que un flujo justifique escribir.
- **Los agentes** leen las fuentes a través de Composio, con el registro que lleva el propio Drive; ningún agente las copia al repositorio.
- **El registro de fuentes** (fecha, remitente, tipo, huella, ubicación) vive en la misma carpeta de Drive, junto a lo que describe.

Consecuencias que hay que atender, porque la decisión las acepta:

- **Composio pasa a ser un tercero que procesa información bajo NDA y datos personales.** Bajo la Ley 1581 de 2012 hay que declararlo a Tu Merch como subencargado y obtener su visto bueno; sin eso, no se cargan insumos con datos personales por esta vía.
- **Disponibilidad:** si Composio falla o cambia sus condiciones, los agentes pierden el acceso a las fuentes. Los originales siguen en Drive, así que el respaldo es acceder a la carpeta directamente.
- **Revocación:** al cerrar el proyecto se revoca la conexión de Composio y se rota su clave, junto con las demás credenciales del cliente (base §6.10).

## Reglas vigentes

- Ningún documento del cliente ni su transcripción se sube al repositorio del proyecto (prohibición 13).
- El material nuevo se guarda en la carpeta de Drive del proyecto y se procesa con `directives/incorporar_fuente.md`; `.tmp/` solo para copias de trabajo temporales.
- Issues y ADR citan las fuentes por fecha, remitente y tipo, sin copiar contenido.

## Pendiente para cerrar este ADR

1. David cambia la visibilidad del repositorio a privado.
2. Crear la carpeta de Drive del proyecto con acceso restringido y conectar Composio a esa carpeta en solo lectura.
3. Declarar Composio a Tu Merch como subencargado y obtener visto bueno; Miguel confirma que cumple el NDA.
4. Decidir si se reescribe el historial de `main` para retirar lo que estuvo público.
