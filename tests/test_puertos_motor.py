"""Los contratos obligan a implementar; los adaptadores aún no ejecutan nada."""
import inspect

import pytest

from motor.adaptadores import proveedores as adaptadores
from motor.puertos import proveedores as puertos


PROVEEDORES = ("Shopify", "Mercately", "Siigo", "Bold", "Drive", "Telegram")
OPERACIONES = (
    ("Shopify", "consultar_producto", "producto-sintetico"),
    ("Mercately", "consultar_conversacion", "contacto-sintetico"),
    ("Mercately", "enviar_plantilla", {}),
    ("Siigo", "consultar_documento", "documento-sintetico"),
    ("Siigo", "crear_borrador", {}),
    ("Bold", "consultar_pago", "referencia-sintetica"),
    ("Drive", "leer_archivo", "archivo-sintetico"),
    ("Telegram", "enviar_alerta", {}),
)


@pytest.mark.parametrize("nombre", PROVEEDORES)
def test_puerto_exige_implementacion_y_adaptador_lo_completa(nombre):
    puerto, adaptador = getattr(puertos, nombre), getattr(adaptadores, nombre)
    with pytest.raises(TypeError):
        puerto()
    assert issubclass(adaptador, puerto)
    assert not inspect.isabstract(adaptador)
    for metodo in puerto.__abstractmethods__:
        assert inspect.signature(getattr(adaptador, metodo)) == inspect.signature(getattr(puerto, metodo))


@pytest.mark.parametrize("proveedor,metodo,entrada", OPERACIONES)
def test_adaptador_falla_explicito_sin_simular_resultados(proveedor, metodo, entrada):
    adaptador = getattr(adaptadores, proveedor)()
    with pytest.raises(NotImplementedError, match="no implementado"):
        getattr(adaptador, metodo)(entrada)


def test_shopify_solo_declara_lectura():
    assert puertos.Shopify.__abstractmethods__ == {"consultar_producto"}
    assert {nombre for nombre in vars(adaptadores.Shopify) if not nombre.startswith("_")} == {
        "consultar_producto",
    }
