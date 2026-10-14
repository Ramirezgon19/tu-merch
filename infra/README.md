# infra/ — despliegue en Docker (ADR-002)

Contrato que `docker-compose.yml` debe cumplir cuando exista. Lo fija [ADR-002](../docs/decisiones/ADR-002-despliegue-en-docker-y-arquitectura-del-motor.md).

- **Portabilidad:** `docker compose up` en una máquina limpia levanta el sistema completo con el mismo `.env` y los mismos volúmenes. Nada depende del host.
- **Estado solo en volúmenes nombrados:** PostgreSQL, datos de n8n y archivos persistentes. `respaldar_volumenes.sh` y `restaurar_volumenes.sh` son parte del entregable y se prueban en la migración simulada antes de la real.
- **Secretos solo en `.env`** en el VPS. `.env.example` lleva todas las claves sin valores.
- **Aislamiento:** red propia; solo el reverse proxy expone puertos; PostgreSQL y n8n no exponen puertos al host.
- **Reproducibilidad:** imágenes fijadas por versión, nunca `latest`. n8n se levanta con los JSON de `workflows/`.
- **Logs** a stdout; alertas a Telegram sin datos personales.

Servicios previstos: reverse proxy con TLS, n8n, PostgreSQL, motor. La versión de cada imagen se fija en el issue de infraestructura, verificada contra la documentación oficial en el momento de hacerlo.
