# ADR-001 · Cronograma e hitos desde el inicio del 15/10

**Estado:** propuesta para aprobación de Brayan. No es decisión aprobada. **Actualizado el 15/10/2026:** el arranque contractual (T) pasa a ser el día en que se reciba el anticipo; ver «Actualización 15/10».
**Fecha:** 12 de octubre de 2026 · **Propone:** Alejo · **Decide:** Brayan (Tu Merch), con David
**Cierra:** P0-02 de `docs/requisitos/base-proyecto.md` §8, en su parte de cronograma por hitos
**Fuentes:** [roadmap aprobado del 01/10/2026](../requisitos/roadmap-aprobado-20261001.md), que declara `GO_LIVE` el 2026-10-29 y la etapa D2 del 15 al 29 de octubre; [propuesta del 01/10/2026](../requisitos/propuesta-aprobada-20261001.md) §2 y §4; paquete de estimación §20 hito 5 y §21; anexo técnico §4.5

## Contexto

Hay tres fechas de salida circulando y ninguna está aprobada por escrito con el nuevo inicio:

| Fecha | De dónde viene | Estado |
|---|---|---|
| 29/10/2026 | §20 hito 5 del cliente, y `GO_LIVE` del roadmap aprobado, que es también la fecha del acta y del segundo 50 % | Compromiso contractual vigente, calculado sobre un arranque el 06/10 que no ocurrió |
| 09/11/2026 | Resultado de aplicar al 15/10 la regla de deslizamiento que la propia propuesta aprobada contiene | Cálculo, no acuerdo |
| 15/11/2026 | Estimación de David del 10/10, ya registrada en la base como orientativa | Tentativa |

La propuesta aprobada previó este caso por escrito: *«El cronograma asume el kickoff el lunes 5 de octubre y los accesos el martes 6; si el arranque ocurre después, el cronograma se desplaza día por día y la fecha de salida se recalcula.»* Invocar esa cláusula es cumplir el acuerdo, no renegociarlo.

La base del proyecto advierte, con razón, que no se deben desplazar las fechas de forma automática, sino reprogramar hitos con sus responsables. El cálculo de abajo es insumo para esa reprogramación, no su resultado.

## Cálculo

El plan expresa los hitos en días hábiles tras el arranque (T): cotizador en sombra en T+5, cierre digital en T+10, piloto de T+11 a T+15 y producción en T+16. Con T = jueves 15/10/2026 y los festivos de Colombia del periodo (2 y 16 de noviembre, 8 y 25 de diciembre):

| Hito | Fecha | Observación |
|---|---|---|
| Arranque, pago inicial y accesos del hito 0 | jue 15/10 | Confirmado por David |
| Construcción del cotizador | 16/10 – 21/10 | Cuatro días hábiles |
| Cotizador en sombra, sin efectos externos | jue 22/10 | Evidencia A01–A09 |
| Construcción del cierre digital | 23/10 – 28/10 | Cuatro días hábiles |
| Cierre digital en lista de permitidos | jue 29/10 | Coincide con la fecha contractual |
| Piloto con revisión humana | vie 30/10 – vie 6/11 | Seis días hábiles |
| Producción | lun 9/11 | T+16 |

El hallazgo que decide el asunto: **el 29/10 cae en T+10, que es la fecha del cierre digital en lista de permitidos, no la de producción.** Sostener producción abierta el 29/10 obligaría a entregar el mínimo viable directo a producción, con cero días de piloto, sin enlace de pago probado y sin emisión fiscal verificada. Eso contradice el recorrido sombra → lista de permitidos → producción que el propio cliente exige en el anexo §4.5, y que la base ya adoptó como WF-00.

## Decisión propuesta

Separar el hito contractual de la apertura a todo el tráfico:

1. El **29/10 se conserva como hito contractual** y se redefine lo que entrega: Fase 1 operando en lista de permitidos con clientes reales autorizados, con evidencia de A01 a A12. La lista de permitidos es operación real, solo acotada.
2. El **acta de aceptación de Fase 1 y el segundo 50 % se firman el 29/10** contra ese hito, como dice la propuesta aprobada.
3. La **apertura a todo el tráfico queda el 9/11**, después del piloto que el cliente pidió.
4. Si alguna dependencia del hito 0 llega después del 15/10, la fecha de producción se reprograma con sus responsables y **el 15/11 de la estimación de David es el margen disponible**, no una fecha adicional.

Esta separación conserva la fecha que el cliente fijó, protege el flujo de caja del mes 1 y no sacrifica el piloto.

## Alternativas descartadas

**Producción abierta el 29/10.** Las palancas existen —recortar el cierre digital al mínimo viable, ruta manual de pago antes del enlace, confirmación de proveedor por formulario, timbrado fiscal por la interfaz de Siigo, expediente solo con enlaces— pero ninguna recupera los siete días de diferencia. La decisión real sería salir sin piloto.

**Mover todo al 15/11 sin hito intermedio.** Deja el mes 1 sin acta hasta mediados de noviembre y, con ello, el segundo 50 % sin fecha. Pierde además el valor de tener una fecha verificable a fin de octubre frente al cliente.

## Consecuencias

- La semana del 3/11 pasa a ser la de la decisión del mes 2, ya con el cierre digital visto en operación, que es lo que la propuesta aprobada pedía. Las nueve tablas de marcación se mueven del 23/10 al 3/11.
- Los pagos del mes 2 se recalculan del 3/11 y 27/11 al 10/11 y 7/12, con D3 del 10/11 al 7/12 y despliegue interno el 24/11.
- La validez de la oferta vence el 30/10 y hay que extenderla en el mismo documento que confirme estas fechas.
- Las fechas de dependencias del cliente que la guía fijaba el 7, 13–14, 15 y 21 de octubre quedan recalculadas en `docs/requisitos/base-proyecto.md` §9 y requieren reconfirmación con cada responsable, una por una. Las 15 dependencias y las 10 decisiones del roadmap (`dep-01`–`dep-15`, `dec-01`–`dec-10`) llevan fechas del 6 y el 7 de octubre que ya pasaron: hay que reemitirlas con el nuevo inicio.
- El roadmap declara como festivos el 12/10, el 2/11 y el 16/11. **Faltan el 8 y el 25 de diciembre**, que entran en juego si D3 se corre a diciembre. Hay que añadirlos antes de recalcular D3.

## Actualización 15/10/2026 · el arranque es el anticipo, no el kickoff

El kickoff ocurrió el jueves 15/10, pero **el anticipo no se ha recibido**. El roadmap aprobado pone «contrato de honorarios firmado y anticipo recibido» como criterio de la etapa K, y la propuesta aprobada dice que, si el arranque ocurre después, el cronograma se desplaza día por día. Por eso **T es el día hábil en que se reciba el anticipo**, no el del kickoff. La tabla del cálculo de arriba sigue siendo válida solo si el anticipo llega el 15/10.

El equipo ya avanza antes de T (sondeo de APIs y contacto QA, issues #19–#22), pero ese trabajo no adelanta las fechas contractuales: se registra como avance a riesgo de Luup Lab.

Mismos desplazamientos en días hábiles, **contando solo lunes a viernes, sin descontar festivos de Colombia** (instrucción de Alejo del 15/10: el cronograma del proyecto no se ajusta por festivos). Esto no cambia la regla de negocio de la vigencia de la cotización, que sí usa festivos (#13).

| Anticipo recibido (T) | Sombra (T+5) | Hito contractual: lista de permitidos, acta y segundo 50 % (T+10) | Piloto (T+11 a T+15) | Producción (T+16) | Decisión mes 2 (T+12) | D3 (T+17 a T+35) |
|---|---|---|---|---|---|---|
| jue 15/10 | jue 22/10 | jue 29/10 | vie 30/10 – jue 5/11 | vie 6/11 | lun 2/11 | lun 9/11 – jue 3/12 |
| vie 16/10 | vie 23/10 | vie 30/10 | lun 2/11 – vie 6/11 | lun 9/11 | mar 3/11 | mar 10/11 – vie 4/12 |
| lun 19/10 | lun 26/10 | lun 2/11 | mar 3/11 – lun 9/11 | mar 10/11 | mié 4/11 | mié 11/11 – lun 7/12 |
| mar 20/10 | mar 27/10 | mar 3/11 | mié 4/11 – mar 10/11 | mié 11/11 | jue 5/11 | jue 12/11 – mar 8/12 |
| jue 22/10 | jue 29/10 | jue 5/11 | vie 6/11 – jue 12/11 | vie 13/11 | lun 9/11 | lun 16/11 – jue 10/12 |

Consecuencias:

- **El 29/10 solo se sostiene si el anticipo llega el 15/10.** Cada día hábil de retraso corre todo un día hábil.
- Sin festivos, la producción con anticipo el 15/10 queda el 6/11, tres días hábiles antes que en el cálculo original (que descontaba el 2/11). Con anticipo hasta el 22/10, la producción sigue antes del margen del 15/11 que estimó David.
- Las fechas de `dep-01`–`dep-15` y `dec-01`–`dec-10` (#4) se reemiten sobre T, no sobre el kickoff.
- La validez de la oferta (30/10) sigue requiriendo extensión en el mismo documento que confirme estas fechas.

## Pendiente para cerrar este ADR

Fecha de recepción del anticipo, que fija T. Confirmación escrita de Brayan sobre los tres puntos: qué entrega el hito del 29/10, que el acta y el pago van contra ese hito, y que la producción abierta queda el 9/11. Sin esa confirmación, la base del proyecto debe seguir marcando la fecha de salida como no aprobada.
