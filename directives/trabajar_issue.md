# Directiva: trabajar un issue

**Objetivo.** Convertir un issue en un cambio verificado sin inventar nada que el issue, las fuentes o las decisiones no digan.

**Entradas.** El número del issue. `gh issue view <n>` lo trae; si `gh` no está autenticado, `gh api repos/Ramirezgon19/tu-merch/issues/<n>`.

**Pasos.**
1. Lee el issue completo. Su **criterio de terminado** es el contrato. Si no es observable y verificable, el issue está mal escrito: coméntalo ahí y detente.
2. Si tiene etiqueta `bloqueado-por-cliente`, revisa en `docs/requisitos/roadmap-aprobado-20261001.md` la dependencia `dep-NN` o decisión `dec-NN` que lo bloquea. Si no está resuelta, detente y dilo.
3. Lee `docs/decisiones/` por si lo que el issue da por abierto ya está decidido, o al revés.
4. Si el issue cita una sección de las fuentes del cliente (§NN, Anexo §N), ábrela. El paquete de estimación está en Drive, enlazado en `docs/fuentes/README.md`; la guía v2 tiene copia en `docs/arquitectura/`.
5. Si toca un efecto externo, lee `cola_operaciones.md`. Si toca `infra/`, lee `despliegue_docker.md`.
6. Busca en `execution/` si ya existe la herramienta que necesitas. Solo si no existe, créala.
7. Escribe el plan antes de codificar: condición verificable, archivos a tocar, cómo mantienes la lógica sin dependencias de HTTP ni de n8n, pruebas que lo demuestran con el nombre del caso si aplica, evidencia que dejarás, rama. **Pide aprobación del plan** si la sesión tiene a alguien al otro lado; si trabajas sin supervisión, deja el plan como primer comentario del issue y sigue.
8. Rama por issue. PR con problema, solución y validación. `python3 execution/verificar_directivas.py` en verde antes de abrirlo.
9. Al cerrar, aplica `cierre_de_bloque.md`.

**Salidas.** Un PR enlazado al issue, con pruebas en verde y evidencia sin datos personales.

**Casos extremos.** Si el criterio no alcanza para construir sin inventar, no rellenes el hueco: propón el comentario para el issue y para. Si descubres una regla de las fuentes que la base no refleja, usa `registrar_decision.md`. Si una tarea no se puede hacer sin tomar una decisión de arquitectura que ADR-002 no cubre, también.
