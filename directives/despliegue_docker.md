# Directiva: despliegue en Docker y migración (ADR-002)

**Objetivo.** Que el stack se levante igual en cualquier VPS, aislado de lo demás, y que migrar sea un procedimiento probado y no una aventura.

**Entradas.** `infra/docker-compose.yml`, `infra/.env.example`, los JSON de `workflows/`.

**Reglas al tocar `infra/`.**
1. Nada en el host: sin paquetes del sistema, sin cron del host, sin rutas absolutas del VPS. Si algo lo requiere, se vuelve contenedor o se documenta como excepción en ADR-002.
2. Estado solo en volúmenes nombrados. Si creas un volumen, añádelo a `execution/respaldar_volumenes.sh` y `execution/restaurar_volumenes.sh` en el mismo PR.
3. Secretos solo en `.env`. Si añades una variable, añádela a `infra/.env.example` sin valor en el mismo PR.
4. Red propia. Solo el reverse proxy expone puertos. PostgreSQL y n8n no exponen puertos al host.
5. Imágenes por versión exacta, verificada contra la documentación oficial al fijarla. Nunca `latest`.
6. n8n se levanta con los JSON de `workflows/`. Un flujo editado en la interfaz y no exportado al repositorio no existe.

**Procedimiento de migración.** Respaldo de volúmenes → copia al VPS destino → `docker compose up` con el mismo `.env` → restauración → verificación con `shadow` → cambio de DNS → verificación en `allowlist` → apagar origen. Se ensaya en una máquina limpia antes de la migración real y la evidencia queda en `docs/operacion/`.

**Acceso del equipo.** SSH por clave, una por persona, revocable una a una. Las claves no se comparten y no viven en el repositorio.

**Casos extremos.** Si el VPS inicial ya aloja otras aplicaciones, confirma que ningún puerto ni volumen colisiona antes de levantar. Si una imagen fija deja de existir, se actualiza la versión en un PR propio con su prueba, no de paso.
