---
description: Lee un issue del cotizador, verifica sus dependencias y propone el plan antes de escribir código
argument-hint: <número de issue>
---

Vas a trabajar el issue **#$1** del cotizador.

No escribas código todavía. Primero:

1. Lee el issue: `gh issue view $1`
2. Lee `docs/requisitos/base-proyecto.md`: su §8 lista los pendientes P0/P1/P2 con responsable y momento. Si este issue depende de uno sin resolver, **detente y dilo**: no construyas sobre un supuesto.
3. Lee `docs/decisiones/`. Puede que lo que el issue da por abierto ya esté decidido en un ADR, o al contrario.
4. Si el issue toca un workflow, lee su fila en el boceto de §5 (WF-00 a WF-14) y respeta su resultado y su bloqueo declarados.
5. Si el issue cita una sección de las fuentes del cliente, ábrela. El paquete de estimación y la guía v2 **no están completos en el repositorio**: los enlaces a los originales están en `docs/fuentes/README.md` y la copia técnica en `docs/arquitectura/guia-integracion-v2.md`.
6. Revisa las secciones 3, 4 y 5 de `CLAUDE.md` y nombra qué restricciones aplican a este issue: arquitectura todavía abierta, cola de operaciones, modo de WF-00, Shopify solo lectura, nada de datos personales.

Luego preséntame, en prosa corta:

- **Qué pide el criterio de terminado**, reformulado como condición verificable.
- **Qué archivos** vas a crear o tocar, y por qué cada uno.
- **Cómo evitas comprometer la arquitectura abierta**: qué queda en lógica sin dependencias y qué queda detrás de un puerto.
- **Qué pruebas** lo demuestran, con el nombre del caso de aceptación si el issue lo referencia.
- **Qué evidencia** hay que dejar, con resultado esperado, obtenido, versión y quién aprueba.
- **Qué es ambiguo.** Si el criterio no alcanza para construir sin inventar, dímelo y propón el comentario que debería ir en el issue.
- **La rama** y el responsable único de la tarea.

Espera mi aprobación antes de codificar.
