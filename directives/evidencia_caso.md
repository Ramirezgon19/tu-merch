# Directiva: evidencia de un caso de aceptación

**Objetivo.** Que la persona comercial o Miguel verifiquen un caso sin volver a pedirnos nada. El cliente escribió que «un enlace a una API no es evidencia».

**Entradas.** El caso: `A01`–`A12` o `M-A01`–`M-A07`. Su definición está en `docs/requisitos/roadmap-aprobado-20261001.md`, tabla de casos, y en la base §9.

**Pasos.**
1. Localiza la prueba automática del caso en `tests/`, con el nombre del caso. Córrela. **Si no existe, detente:** la evidencia de un caso sin prueba no es evidencia.
2. Genera el documento con `execution/generar_evidencia.py <caso>` cuando exista; mientras tanto, escríbelo a mano con la misma estructura en `docs/operacion/evidencia/<etapa>-casos.md`.
3. Estructura por caso: qué exige, citando la fuente; cómo se verifica, con archivo, función y comando; la salida pegada tal cual; **resultado esperado frente a obtenido**; versión de las reglas aplicadas y quién aprueba; limitaciones si se cubre parcialmente. Para integraciones, request y response reales anonimizados.
4. Antes de guardar, busca nombres de clientes, NIT, teléfonos, correos, RUT, direcciones, números de los contactos QA, api-keys o tokens. Reemplaza por un marcador. El repositorio está bajo NDA.

**Salidas.** Una sección en el documento de evidencia de la etapa, enlazada desde el PR.
