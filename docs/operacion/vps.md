# Inventario del VPS inicial

**Issue:** #6 · **Levantado:** 13/10/2026 por Alejo, con comandos de solo lectura · **Fuente:** ADR-002, `directives/despliegue_docker.md`

> El repositorio es público. Este documento no lleva IP, nombres de host, claves, rutas de otros proyectos ni puertos internos ajenos a Tu Merch. Esos datos los tiene Alejo y se comparten por canal privado.

## Máquina

| Elemento | Valor |
|---|---|
| Proveedor y plan | Hostinger, KVM 1, centro de datos de Boston |
| Sistema | Ubuntu 24.04.4 LTS, kernel 6.8 |
| CPU | 1 vCPU |
| RAM | 3,8 GiB; 1,7 GiB en uso y 2,1 GiB disponibles con los stacks actuales |
| Disco | 48 GB; 29 GB usados (60 %) y 20 GB libres |
| Docker | 29.5.3, con Compose v5.1.4 |
| Seguridad del host | `ufw` activo, que solo permite 22, 80 y 443; `fail2ban` con la jaula `sshd`; agente antimalware del proveedor |

## Qué más corre ahí

El VPS es **compartido**. Hay cuatro proyectos de Compose ajenos a Tu Merch: dos instancias de n8n, un stack con reverse proxy y otro servicio en bucle de reinicio. Además hay tres contenedores detenidos y un proceso del host, fuera de Docker, que escucha solo en la interfaz local. Ninguno pertenece a Tu Merch y ninguno se reutiliza (ADR-002).

Puntos que afectan el despliegue de Tu Merch:

1. **Los puertos 80 y 443 ya los tiene el reverse proxy de otro stack**, que también gestiona los certificados. La regla 4 de `directives/despliegue_docker.md` dice que solo el reverse proxy expone puertos, así que Tu Merch no puede levantar el suyo en 80/443 sin colisionar. Hace falta decidir cómo entra el tráfico público (webhooks de Mercately, Shopify, pagos): ver «Decisiones pendientes».
2. **No hay colisión de nombres** entre los volúmenes y las redes existentes y los que usará el proyecto de Compose `tu-merch`, siempre que todos lleven ese prefijo.
3. **La capacidad es justa.** Con 1 vCPU y unos 2 GiB libres, n8n, PostgreSQL y el motor caben, pero compiten por CPU con otras dos instancias de n8n y con un contenedor que se reinicia sin parar. Hay que fijar límites de memoria en el `docker-compose.yml` y medir antes del piloto.
4. **Dominio y TLS:** todavía no hay un dominio asignado a Tu Merch. Los certificados actuales los emite el reverse proxy existente.
5. **Respaldo:** no hay política de respaldo de volúmenes en el host. La de Tu Merch se construye con los scripts de ADR-002.

## Acceso

| Elemento | Estado al 13/10 |
|---|---|
| Usuarios con shell | Solo `root` |
| Claves autorizadas | Una, la de Alejo |
| David | Sin acceso |
| Claude Code | Entra con la clave de Alejo desde su Mac |

**Pendiente para cerrar el issue:** crear un usuario por persona con su propia clave, probar el acceso de cada uno y decidir si `root` deja de aceptar SSH.

**Ruta de red:** desde algunas redes con CGNAT, el VPS no es alcanzable por IPv4 y sí por IPv6. Ver el aprendizaje del 13/10 en `CLAUDE.md`.

## Decisiones pendientes

- **Entrada pública (80/443).** Hay tres opciones: (a) agregar un sitio para Tu Merch en el reverse proxy existente, lo que acopla Tu Merch a otro stack; (b) sacar el reverse proxy a un stack propio de borde, compartido por todos los proyectos del VPS; (c) usar otro VPS. Se registra con `directives/registrar_decision.md` antes de escribir `infra/docker-compose.yml`.
- **Usuarios y Docker.** Pertenecer al grupo `docker` equivale en la práctica a ser `root`. Hay que decidir si los usuarios del equipo lo tienen o si usan `sudo` con registro.
