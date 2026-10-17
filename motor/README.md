# Motor de cotización

Estructura inicial del issue #9, siguiendo ADR-002:

| Paquete | Responsabilidad |
|---|---|
| `dominio/` | Modelos y reglas puras, sin proveedores ni transporte. |
| `aplicacion/` | Casos de uso que coordinan el dominio y los puertos. |
| `puertos/` | Contratos abstractos para Shopify, Mercately, Siigo, Bold, Drive y Telegram. |
| `adaptadores/` | Implementaciones de esos contratos; todas lanzan `NotImplementedError` por ahora. |

El dominio solo importa módulos de `motor.dominio` y una lista explícita de
módulos estándar sin transporte, definida en `tests/test_arquitectura_motor.py`.
La prueba analiza también imports relativos, condicionales y dentro de funciones;
no importa ni ejecuta los módulos inspeccionados. Una nueva dependencia estándar
requiere revisar esa lista. `motor/__init__.py` también se comprueba porque se
ejecuta al importar cualquier subpaquete.

Los puertos son mínimos y sus cargas de datos son provisionales: cada integración
concretará sus contratos con esquemas y pruebas. Shopify solo expone lectura.
Drive representa lectura de archivos; su futura implementación utilizará el
puente acordado en ADR-003. Declarar un método de escritura no autoriza invocarlo:
su integración deberá pasar por la cola WF-00 del issue #10, todavía pendiente.
No hay clientes HTTP, credenciales, cálculo de precios ni servicios ejecutables.

Desde la raíz del repositorio, con Python 3.9 o posterior:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m pytest -q
python3 execution/verificar_directivas.py
```

Las pruebas usan datos sintéticos y no requieren acceso a proveedores. Además
del análisis del dominio real, casos deliberadamente inválidos comprueban que
el control detecta imports de HTTP, n8n, SDK de proveedor y otras capas. Los
contratos abstractos y cada método de los adaptadores se verifican por separado.
