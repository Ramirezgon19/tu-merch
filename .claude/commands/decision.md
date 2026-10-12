---
description: Registra un ADR cuando una regla o una arquitectura no está decidida, en vez de resolverla en código
argument-hint: <tema de la decisión>
---

Hay una duda sobre: **$ARGUMENTS**

Esto no se resuelve en código. Haz lo siguiente:

1. Busca el tema en `docs/requisitos/base-proyecto.md`: la tabla de §3 separa lo confirmado por las fuentes de lo que falta cerrar, y §8 lista los pendientes P0/P1/P2 con su responsable. **Si ya está ahí, no abras nada nuevo:** dime cuál es, quién decide, para cuándo, y si está vencido.
2. Revisa `docs/decisiones/`. Puede existir ya un ADR, aprobado o en propuesta.
3. Si no existe, redacta un ADR nuevo en `docs/decisiones/ADR-NNN-<slug>.md`, con el número siguiente disponible, y esta estructura: estado (propuesta o aprobado, nunca ambiguo), fecha, quién propone y quién decide, qué pendiente cierra, fuentes citadas por sección, contexto, alternativas con su consecuencia técnica, decisión propuesta, consecuencias y qué falta para cerrarlo.
4. Abre el issue que lo acompaña con `gh issue create`, enlazando el ADR, con el responsable de la decisión según §8 y la fecha que propones.
5. Si la decisión bloquea un issue abierto, coméntalo ahí y márcalo bloqueado.

Dos reglas duras. **No propongas un valor por defecto «razonable» dentro del código** mientras la decisión esté abierta: un número inventado en una cotización se descubre facturando. Y **no escribas el ADR como si estuviera aprobado**: mientras nadie lo confirme, su estado es propuesta.
