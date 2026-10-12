---
description: Cierra un bloque de trabajo siguiendo cierre_de_bloque.md
allowed-tools: Bash(git log:*), Bash(git status:*), Bash(gh api:*), Bash(python3 execution/verificar_directivas.py:*)
---
Commits recientes:
!`git log --since="3 days ago" --pretty=format:"%h %ad %an %s" --date=short`

Rama y trabajo sin confirmar:
!`git status --short --branch`

Sigue `directives/cierre_de_bloque.md`: escribe el registro de cierre (qué cambió, cómo se verificó, qué falta, qué se necesita), registra el aprendizaje si lo hubo en `CLAUDE.md`, y corre `python3 execution/verificar_directivas.py --arreglar`. Revisa que nada lleve datos personales.
