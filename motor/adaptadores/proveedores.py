"""Adaptadores pendientes: ninguna operación devuelve éxitos ficticios."""
from typing import Mapping, Sequence

from motor.puertos import proveedores


class Shopify(proveedores.Shopify):
    def consultar_producto(self, producto_id: str) -> Mapping[str, object]:
        raise NotImplementedError("Shopify: no implementado")


class Mercately(proveedores.Mercately):
    def consultar_conversacion(self, contacto_id: str) -> Sequence[Mapping[str, object]]:
        raise NotImplementedError("Mercately: no implementado")

    def enviar_plantilla(self, operacion: Mapping[str, object]) -> str:
        raise NotImplementedError("Mercately: no implementado")


class Siigo(proveedores.Siigo):
    def consultar_documento(self, documento_id: str) -> Mapping[str, object]:
        raise NotImplementedError("Siigo: no implementado")

    def crear_borrador(self, operacion: Mapping[str, object]) -> str:
        raise NotImplementedError("Siigo: no implementado")


class Bold(proveedores.Bold):
    def consultar_pago(self, referencia: str) -> Mapping[str, object]:
        raise NotImplementedError("Bold: no implementado")


class Drive(proveedores.Drive):
    def leer_archivo(self, archivo_id: str) -> bytes:
        raise NotImplementedError("Drive: no implementado")


class Telegram(proveedores.Telegram):
    def enviar_alerta(self, operacion: Mapping[str, object]) -> str:
        raise NotImplementedError("Telegram: no implementado")
