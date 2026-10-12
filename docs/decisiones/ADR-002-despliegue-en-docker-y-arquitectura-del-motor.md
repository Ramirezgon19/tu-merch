# ADR-002 · Despliegue en Docker sobre VPS de Luup Lab y arquitectura del motor

**Estado:** decidido por Alejo el 12/10/2026; pendiente de revisión de David. Cierra la pregunta de arquitectura que la base dejaba abierta en §4 y que `CLAUDE.md` marcaba como «no la supongas».
**Fecha:** 12 de octubre de 2026 · **Decide:** Alejo · **Revisa:** David · **Informa:** Miguel, como revisor técnico del cliente
**Cierra:** P0-03 de `docs/requisitos/base-proyecto.md` §8 en su parte de arquitectura; P1-05 en su parte de recursos del VPS
**Fuentes:** base §4 (propuesta de n8n en VPS Hostinger de Luup Lab con motor propio); anexo técnico §2 (FastAPI, PostgreSQL y extractor Gemini existentes de Tu Merch) y §4.6 (entrega en su repositorio con workflows JSON)

## Decisión

1. **La solución corre en contenedores Docker sobre un VPS de Luup Lab**, aislada del resto de aplicaciones que ese VPS aloja. Inicialmente es un VPS personal; **el conjunto de contenedores migrará a otro VPS** más adelante, y esa migración se diseña desde el primer día, no se improvisa después.
2. **El motor de cotización es propio**, con persistencia en PostgreSQL, separado de los adaptadores de canal. **n8n orquesta.** Esto adopta la propuesta de la base §4 y la convierte en decisión. La plataforma FastAPI existente de Tu Merch no se reutiliza como runtime; si Miguel autoriza acceso, se consulta como referencia de contratos y del extractor Gemini, nada más.
3. **El equipo accede por SSH al VPS** para entrar a los contenedores cuando haga falta. El acceso es por clave, una por persona, revocable una a una.

## Reglas que se derivan, y que valen desde el primer commit de código

**Portabilidad.** Todo lo que corre se declara en `infra/docker-compose.yml`. Ninguna dependencia vive en el host: ni paquetes del sistema, ni cron del host, ni rutas absolutas del VPS, ni un nginx del host que haga de proxy a mano. Si algo requiere el host, se vuelve un contenedor o se documenta como excepción en este ADR. La prueba de portabilidad es una sola: `docker compose up` en una máquina limpia levanta el sistema completo con el mismo `.env` y los mismos volúmenes.

**Estado solo en volúmenes nombrados.** PostgreSQL, los datos de n8n y cualquier archivo que deba sobrevivir viven en volúmenes con nombre, nunca en el sistema de archivos del contenedor ni en rutas sueltas del host. La migración a otro VPS es: respaldo de volúmenes, copia, restauración, cambio de DNS. `execution/respaldar_volumenes.sh` y `execution/restaurar_volumenes.sh` son parte del entregable de infraestructura, no un extra.

**Secretos fuera de las imágenes.** Van en `.env` en el VPS, nunca en imágenes, en `docker-compose.yml` ni en el repositorio. El repositorio lleva `.env.example` con todas las claves y ningún valor. La llave de Mercately, las credenciales de Siigo y Shopify y el token de Telegram son del cliente y se rotan al cierre del proyecto, como ya exige la base §6.10.

**Aislamiento.** Red de Docker propia del proyecto. Solo los puertos estrictamente necesarios se exponen, y solo al reverse proxy; PostgreSQL y n8n no exponen puertos al host. Las otras aplicaciones del VPS no ven ni comparten nada con este stack.

**Reproducibilidad.** Las imágenes se fijan por versión, no por `latest`. Las exportaciones JSON de n8n van en `workflows/` y deben coincidir con lo desplegado, como exige el anexo §4.6; el contenedor de n8n se levanta con esos JSON, no con flujos creados a mano en la interfaz y olvidados ahí.

**Observabilidad mínima.** Logs a stdout de cada contenedor, recogidos por Docker; alertas operativas al bot de Telegram del cliente como ya prevé WF-12. Sin datos personales en ningún log.

## Consecuencia contractual, que no es técnica

Al correr sobre infraestructura de Luup Lab, los datos personales y fiscales de los clientes de Tu Merch pasan por un sistema que Luup Lab controla. Bajo la Ley 1581 de 2012, Luup Lab deja de ser solo proveedor y actúa como **encargado del tratamiento**, con obligaciones propias de seguridad, de conservación y de devolución o supresión al terminar. Esto obliga a tres cosas:

- La cláusula de datos personales del contrato de honorarios debe reflejarlo, y la de salida debe prever la devolución de volúmenes y la supresión certificada.
- El costo del VPS y su respaldo es un costo recurrente de operación que, según la propuesta aprobada, corre por cuenta de Tu Merch; hay que acordarlo por escrito y no absorberlo en silencio.
- La migración final, si el contenedor termina en infraestructura del cliente, es la salida natural prevista por el anexo §4.6 y debe quedar como entregable, con su procedimiento probado.

## Alternativas descartadas

**Módulo dentro de la plataforma FastAPI de Tu Merch.** Era la lectura del plan del 30/09. Depende de un acceso que no se ha autorizado, de productivizar una plataforma que el anexo describe en sombra y sin terminar, y de que Miguel revise despliegues sobre su infraestructura con un equipo que no desarrolla. El costo de coordinación es alto y el control sobre los tiempos, bajo.

**Instalación directa en el VPS sin contenedores.** Más rápida el primer día, imposible de migrar limpiamente y contaminada por lo que ya corre en ese VPS. Contradice el requisito de migración.

## Pendiente para cerrar este ADR

- Revisión de David, que es quien propuso la arquitectura base.
- Inventario del VPS inicial: versión de Docker, recursos, dominio y TLS, política de respaldo. Es el P1-05 de la base y entra como issue de infraestructura.
- Decisión escrita con Tu Merch sobre quién paga el VPS y dónde termina el contenedor al cierre.
