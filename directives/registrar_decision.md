# Directiva: registrar una decisión (ADR)

**Objetivo.** Que ninguna regla de negocio ni elección de arquitectura se resuelva en código por conveniencia. Un número inventado en una cotización se descubre facturando.

**Entradas.** El tema. La sección de la fuente que lo origina.

**Pasos.**
1. Busca el tema en `docs/requisitos/base-proyecto.md` §3 (confirmado frente a pendiente) y §8 (P0/P1/P2 con responsable), y en `docs/requisitos/roadmap-aprobado-20261001.md` (`dec-01`–`dec-10`). **Si ya existe, no abras nada:** di cuál es, quién decide, para cuándo y si está vencido.
2. Revisa `docs/decisiones/`. Puede haber un ADR aprobado o en propuesta.
3. Si no existe, escribe `docs/decisiones/ADR-NNN-<slug>.md` con el siguiente número libre y esta estructura: **Estado** (propuesta o decidido, nunca ambiguo; y quién lo decidió), fecha, propone, decide, qué pendiente cierra, fuentes por sección, contexto, decisión, reglas que se derivan, alternativas descartadas, consecuencias, qué falta para cerrarlo.
4. Abre el issue que lo acompaña, etiqueta `tipo:decision`, enlazando el ADR, con el responsable según la fuente y la fecha que propones.
5. Si bloquea un issue abierto, coméntalo ahí y márcalo bloqueado.

**Salidas.** Un ADR y un issue.

**Reglas duras.** No pongas un valor por defecto «razonable» en el código mientras la decisión esté abierta. No escribas un ADR en propuesta como si estuviera aprobado. Mantén los ADR existentes: se actualizan con una entrada nueva en su estado, no se sobreescriben.
