# Cotizador automático · Tu Merch × Luup Lab

Repositorio privado de documentación y desarrollo del cotizador. Estado al **12/10/2026: diseño; alcance contractual aprobado; sin workflows implementados ni despliegue**.

## Empezar aquí

Leer la [base del proyecto](docs/requisitos/base-proyecto.md): requisitos, fuentes, arquitectura propuesta, 15 workflows, dependencias, decisiones pendientes y pruebas de aceptación. Versión documental actual: **0.4**.

Consultar el [roadmap aprobado del 01/10/2026](docs/requisitos/roadmap-aprobado-20261001.md), que es el artefacto que Tu Merch aprobó y la autoridad en alcance, entregables, criterios y fechas, con su [HTML original](docs/requisitos/20261001_Roadmap_Cotizador_TuMerch.html) al lado; la [propuesta](docs/requisitos/propuesta-aprobada-20261001.md) que lo respalda en honorarios y condiciones; y las [decisiones registradas](docs/decisiones/). Para el entorno, el [índice de fuentes en Drive](docs/fuentes/README.md) y la [guía técnica de integración v2](docs/arquitectura/guia-integracion-v2.md) del cliente. Los originales permanecen en Drive; la copia técnica del repositorio se actualiza manualmente.

Quien trabaje con agentes de código debe leer [`CLAUDE.md`](CLAUDE.md), que Claude Code carga al abrir una sesión en la raíz, o [`AGENTS.md`](AGENTS.md) para los agentes que leen ese nombre.

**Nomenclatura:** «v2» designa la guía técnica del cliente del 08/10. La propuesta de Luup Lab se cita por su fecha, 01/10/2026.

## Alcance

- **Fase 1:** solicitud sin marcación, catálogo y disponibilidad, cálculo, cotización, envío, pago confirmado, pedido al proveedor, facturación con aprobaciones fiscales y trazabilidad.
- **Fase 2:** marcación y arte, tablas técnicas y apoyo al vendedor.
- Orquestación prevista: **n8n en VPS Hostinger de Luup Lab**. Arquitectura del motor y persistencia todavía por acordar.

## Equipo y fechas

| Tema | Estado |
|---|---|
| Inicio | 15 de octubre de 2026 |
| Hito contractual de Fase 1 | 29 de octubre de 2026, en lista de permitidos; propuesto en ADR-001, pendiente de confirmación de Brayan |
| Producción abierta | 9 de noviembre de 2026 propuesto, con margen hasta el 15; tentativa, pendiente de cronograma acordado |
| Desarrollo confirmado | Alejo y David; responsabilidades por repartir |
| Juanfe | Participación pendiente |
| Miguel Tusso | Revisor técnico de Tu Merch, empresa contratante; no desarrolla |
| Forma de trabajo | Asíncrona |
| Calculadora | Pendiente de Brayan; no bloquea el diseño, requerida para validar descuentos reales |

## Trabajo asíncrono

Cada tarea debe registrar resultado esperado, responsable, estado, dependencias, evidencia y siguiente acción. Al terminar un bloque, dejar qué cambió, cómo se verificó y qué falta para continuar. Mantener las decisiones propuestas separadas de las aprobadas.

Crear ramas para cambios de desarrollo y presentar pull requests con problema, solución y validación. El despliegue en la infraestructura de Tu Merch requiere revisión técnica, evidencia de pruebas y respaldo. Las exportaciones JSON de n8n deberán coincidir con la versión del repositorio que se despliega.

## Organización

| Ruta | Uso |
|---|---|
| `docs/fuentes/` | Índice de enlaces a los originales de Drive |
| `docs/requisitos/` | Base y requisitos del proyecto; ya iniciada |
| `docs/arquitectura/`, `docs/decisiones/`, `docs/operacion/` | Diseños, decisiones y procedimientos; crear al documentarlos |
| `workflows/`, `motor/`, `schemas/`, `tests/` | Flujos n8n, lógica, contratos y pruebas; crear al implementarlos |
| `infra/`, `config/` | Despliegue y configuración sin secretos; crear cuando se definan |

## Próximo trabajo

1. Detallar WF-01 a WF-06: detectar solicitud, estructurar datos, validar catálogo, calcular, generar documento y enviar.
2. Definir contrato JSON, estados, deduplicación y manejo de excepciones.
3. Acordar disparador CRM y convivencia con MIA; preparar validación de Siigo, pagos y proveedores.
4. Incorporar y validar los descuentos cuando Brayan entregue el Excel.

## Datos y controles

No guardar tokens, contraseñas, enlaces de secretos, RUT, conversaciones ni documentos de clientes en el repositorio. El `.gitignore` ayuda a excluir archivos locales, pero cada cambio debe revisarse antes de publicarlo.

Shopify se consulta en modo lectura. Las pruebas de Mercately se limitan a contactos y negociaciones autorizados. La operación comenzará registrando lo que haría sin efectos externos y avanzará a pruebas autorizadas antes de producción.

La documentación fuente está bajo NDA. Conservar sus referencias y permisos privados; no redistribuir públicamente. Al cierre, la entrega incluye repositorio completo, workflows JSON, variables documentadas sin valores y procedimientos de despliegue y recuperación.
