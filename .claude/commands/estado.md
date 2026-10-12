---
description: Arma el registro de cierre de bloque del cotizador desde git y los issues
allowed-tools: Bash(git log:*), Bash(git status:*), Bash(gh issue list:*), Bash(gh pr list:*)
---

Commits recientes:
!`git log --since="3 days ago" --pretty=format:"%h %ad %an %s" --date=short`

Rama y trabajo sin confirmar:
!`git status --short --branch`

Issues abiertos:
!`gh issue list --state open --limit 40 --json number,title,labels,assignees --jq '.[] | "#\(.number) \(.title) — \([.labels[].name] | join(","))"'`

PRs abiertos:
!`gh pr list --state open --json number,title,isDraft --jq '.[] | "#\(.number) \(.title)\(if .isDraft then " (borrador)" else "" end)"'`

Con eso, escribe el registro de cierre de bloque en el formato que pide `docs/requisitos/base-proyecto.md`: **qué cambió, cómo se verificó, qué queda pendiente y qué decisión o dato se necesita.** En prosa, concreto, separando lo que está listo para continuar de lo bloqueado por terceros.

Luego:

1. Verifica que no haya datos personales ni fiscales en el texto, porque esto se comparte con el cliente.
2. Dime si algún pendiente P0 de §8 lleva más de dos días hábiles vencido frente a su momento comprometido. Eso se escala, no se espera.
3. Si lo que ves en el repositorio contradice la base, dímelo y propón la entrada de historial de cambios que correspondería, sin escribirla tú.
4. Mantén separado lo propuesto de lo aprobado. Una fecha o una arquitectura sin ADR confirmado es propuesta.
