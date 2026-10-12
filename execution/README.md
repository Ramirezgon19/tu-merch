# execution/ — herramientas deterministas del proyecto

Scripts con los que el equipo y los agentes operan el proyecto. No son el producto: el motor va en `motor/` y los flujos en `workflows/`.

| Script | Para qué | Directiva |
|---|---|---|
| `verificar_directivas.py` | Falla si `CLAUDE.md`, `AGENTS.md` y `GEMINI.md` difieren. `--arreglar` los iguala desde `CLAUDE.md` | todas |
| `cargar_issues.py` | Crea etiquetas, hitos e issues en GitHub desde un JSON, por la API REST, sin duplicar | `trabajar_issue.md` |

Convenciones: Python 3.9+, sin dependencias fuera de la biblioteca estándar salvo que la directiva lo justifique, `.env` para secretos, salidas intermedias en `.tmp/`. Cada script explica su uso en el docstring y devuelve código de salida distinto de cero cuando falla.
