# Directiva: cierre de un bloque de trabajo

**Objetivo.** Que la siguiente persona o agente pueda continuar sin preguntar. Es la regla de trabajo asíncrono de la base.

**Pasos.**
1. Escribe en el issue, o en el PR si es el cierre del issue: **qué cambió, cómo se verificó, qué queda pendiente y qué decisión o dato se necesita.** Prosa concreta. Separa lo listo para continuar de lo bloqueado por terceros.
2. Si algo de lo que viste contradice `docs/requisitos/base-proyecto.md`, propón la entrada de historial correspondiente; no la escribas sin acuerdo.
3. Si aprendiste algo no trivial —una restricción de API, un límite real, un supuesto falso, un gotcha del entorno—, añádelo a la sección de aprendizajes de `CLAUDE.md` y corre `python3 execution/verificar_directivas.py --arreglar` para replicarlo a `AGENTS.md` y `GEMINI.md`.
4. Si cambiaste una directiva, deja en su encabezado la fecha y qué cambió.
5. Verifica que nada de lo que escribiste lleva datos personales ni fiscales.

**Salida.** Un registro de cierre y, si aplica, un aprendizaje nuevo replicado en los tres archivos de agente.
