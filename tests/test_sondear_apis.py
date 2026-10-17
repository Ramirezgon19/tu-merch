"""Regresiones de privacidad del sondeo; solo datos sintéticos, sin red."""
import contextlib
import importlib.util
import io
import pathlib
import unittest
from unittest.mock import patch
from urllib.error import HTTPError


spec = importlib.util.spec_from_file_location(
    "sondear_apis", pathlib.Path(__file__).resolve().parents[1] / "execution/sondear_apis.py"
)
sondeo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sondeo)


class PrivacidadSondeo(unittest.TestCase):
    def test_error_http_no_conserva_ni_imprime_datos_reflejados(self):
        error = HTTPError("https://example.invalid", 422, "error", {},
                          io.BytesIO(b'{"phone":"QA-SINTETICO"}'))
        salida = io.StringIO()
        with patch.object(sondeo.urllib.request, "urlopen", side_effect=error):
            estado, cuerpo = sondeo.pedir("GET", "https://example.invalid", {})
        self.assertEqual(estado, 422)
        self.assertNotIn("QA-SINTETICO", str(cuerpo))
        with contextlib.redirect_stdout(salida):
            sondeo.imprimir("Contacto QA", estado, {"error_http": "QA-SINTETICO"})
        self.assertNotIn("QA-SINTETICO", salida.getvalue())
        self.assertIn("HTTP 422", salida.getvalue())

    def test_rutas_adicionales_no_imprimen_identificadores(self):
        ruta = "/customers/QA-SINTETICO/whatsapp_conversations?cursor=CURSOR-SECRETO"
        salida = io.StringIO()
        with patch.dict(sondeo.os.environ, {"MERCATELY_API_KEY": "clave-sintetica"}, clear=True), \
                patch.object(sondeo, "pedir", return_value=(200, {"name": "NOMBRE-SINTETICO"})) as pedir, \
                patch.object(sondeo.time, "sleep"), contextlib.redirect_stdout(salida):
            sondeo.sondear_mercately([ruta])
        self.assertTrue(pedir.call_args.args[1].endswith(ruta))
        for sensible in ("QA-SINTETICO", "CURSOR-SECRETO", "NOMBRE-SINTETICO", "clave-sintetica"):
            self.assertNotIn(sensible, salida.getvalue())
        self.assertIn("Ruta adicional 1", salida.getvalue())
        self.assertIn("HTTP 200", salida.getvalue())


if __name__ == "__main__":
    unittest.main()
