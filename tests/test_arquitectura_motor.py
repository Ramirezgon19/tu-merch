"""La frontera del dominio se verifica sin importar el código inspeccionado."""
import ast
from importlib.util import resolve_name
from pathlib import Path

import pytest


RAIZ = Path(__file__).resolve().parents[1]
ESTANDAR_PERMITIDA = {
    "__future__", "abc", "collections", "dataclasses", "datetime", "decimal",
    "enum", "fractions", "functools", "itertools", "math", "numbers",
    "operator", "re", "statistics", "string", "typing", "uuid", "zoneinfo",
}


def imports_prohibidos(codigo, paquete):
    """Permite solo el propio dominio y módulos estándar revisados."""
    errores = []
    for nodo in ast.walk(ast.parse(codigo)):
        if isinstance(nodo, ast.Import):
            modulos = [alias.name for alias in nodo.names]
        elif isinstance(nodo, ast.ImportFrom):
            nombre = "." * nodo.level + (nodo.module or "")
            try:
                modulos = [resolve_name(nombre, paquete) if nodo.level else nombre]
            except ImportError:
                errores.append((nodo.lineno, nombre))
                continue
        elif isinstance(nodo, ast.Call) and isinstance(nodo.func, ast.Name) \
                and nodo.func.id == "__import__":
            errores.append((nodo.lineno, "__import__"))
            continue
        else:
            continue
        for modulo in modulos:
            if not (modulo == "motor.dominio" or modulo.startswith("motor.dominio.")
                    or modulo.split(".")[0] in ESTANDAR_PERMITIDA):
                errores.append((nodo.lineno, modulo))
    return errores


def test_dominio_y_raiz_no_importan_transporte_ni_otras_capas():
    archivos = sorted((RAIZ / "motor/dominio").rglob("*.py"))
    assert archivos, "Debe existir el paquete de dominio"
    archivos.append(RAIZ / "motor/__init__.py")
    errores = []
    for archivo in archivos:
        paquete = ".".join(archivo.relative_to(RAIZ).parent.parts)
        for linea, modulo in imports_prohibidos(archivo.read_text(encoding="utf-8"), paquete):
            errores.append(f"{archivo.relative_to(RAIZ)}:{linea}: {modulo}")
    assert not errores, "Dependencias prohibidas en el dominio:\n" + "\n".join(errores)


@pytest.mark.parametrize("codigo", [
    "import http.client", "from urllib.request import urlopen",
    "import requests", "import n8n", "import shopify", "import mercately",
    "from motor.adaptadores import proveedores", "from motor.puertos import proveedores",
    "from ..adaptadores import proveedores", "from .. import adaptadores",
    "def consultar():\n    import http.client",
    "from typing import TYPE_CHECKING\nif TYPE_CHECKING:\n    import requests",
    "__import__('requests')", "import importlib",
])
def test_control_rechaza_dependencias_prohibidas(codigo):
    assert imports_prohibidos(codigo, "motor.dominio")


@pytest.mark.parametrize("codigo", [
    "from decimal import Decimal", "import datetime, dataclasses",
    "from . import modelos", "from motor.dominio import modelos",
    "from .modelos import Cotizacion", "from __future__ import annotations",
    '# import requests\ntexto = "import n8n"',
])
def test_control_permite_dominio_y_biblioteca_estandar(codigo):
    assert imports_prohibidos(codigo, "motor.dominio") == []
