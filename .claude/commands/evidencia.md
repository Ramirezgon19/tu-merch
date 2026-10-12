---
description: Arma la evidencia de un caso de aceptación A01-A12 o M-A01-M-A07
argument-hint: <caso, p.ej. A03 o M-A02>
---

Vas a documentar la evidencia del caso **$1**.

El cliente escribió que un enlace a una API no es evidencia. La evidencia es lo que permite que la persona comercial o Miguel verifiquen el caso sin volver a pedirnos nada.

1. Busca el caso en la tabla de §9 de `docs/requisitos/base-proyecto.md`, que relaciona cada evidencia con sus casos funcionales, y en la fila del workflow correspondiente en §5.
2. Localiza y corre la prueba automática del caso. Si no existe, dímelo y no sigas: la evidencia de un caso sin prueba no es evidencia.
3. Escribe o actualiza el documento de evidencia en `docs/operacion/evidencia/`, creando la carpeta si no existe, con una sección por caso que contenga: qué exige el caso citando la fuente; cómo se verifica, con el archivo y la función de prueba y el comando; la salida pegada tal cual; los datos de entrada y el **resultado esperado frente al obtenido**; la versión de las reglas aplicadas y quién aprueba; y las limitaciones si el caso se cubre parcialmente.
4. Para casos de integración, incluye el request y el response reales anonimizados.

Antes de guardar, revisa línea por línea buscando nombres de clientes, NIT, teléfonos, correos, RUT, direcciones, los números de los contactos QA, api-keys o tokens. Reemplaza lo que encuentres por un marcador. Este repositorio está bajo NDA y la base prohíbe expresamente guardar conversaciones, teléfonos QA, RUT y documentos de clientes.
