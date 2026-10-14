# ADR-003 · Dónde se almacenan las fuentes y los insumos del cliente

**Estado:** propuesta. Requiere decisión de Alejo y David, y confirmación de Miguel sobre el NDA.
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

**Propuesta:** **B** para documentos y transcripciones, y para los insumos con datos personales, anonimización antes de cualquier repositorio y el original en el mismo repo privado de fuentes con acceso solo para quienes lo necesiten. **D se descarta** por el intermediario adicional; **E se descarta** por ampliar el acceso a producción. **C** queda como respaldo de lo que el cliente comparte por Drive, no como lugar de trabajo.

El registro de fuentes (fecha, remitente, tipo, huella del archivo, ubicación) vive en el repo de fuentes, junto a lo que describe.

## Reglas mientras no se decida

- Ningún documento del cliente ni su transcripción se sube al repositorio del proyecto (prohibición 13).
- El material nuevo se procesa en `.tmp/` con `directives/incorporar_fuente.md`.
- Issues y ADR citan las fuentes por fecha, remitente y tipo, sin copiar contenido.

## Pendiente para cerrar este ADR

1. David cambia la visibilidad del repositorio a privado.
2. Alejo y David eligen entre A y B.
3. Miguel confirma por escrito que el almacenamiento elegido cumple el NDA.
4. Se decide si se reescribe el historial de `main` para retirar lo que estuvo público.
