"""Puertos iniciales; los contratos de datos se concretan en cada integración.

Las operaciones de escritura se invocarán exclusivamente desde la cola WF-00.
Shopify solo declara consultas.
"""
from abc import ABC, abstractmethod
from typing import Mapping, Sequence


class Shopify(ABC):
    """Lectura del catálogo; no expone operaciones de escritura."""

    @abstractmethod
    def consultar_producto(self, producto_id: str) -> Mapping[str, object]:
        raise NotImplementedError


class Mercately(ABC):
    """Lectura de conversaciones y envío de plantillas desde WF-00."""

    @abstractmethod
    def consultar_conversacion(self, contacto_id: str) -> Sequence[Mapping[str, object]]:
        raise NotImplementedError

    @abstractmethod
    def enviar_plantilla(self, operacion: Mapping[str, object]) -> str:
        raise NotImplementedError


class Siigo(ABC):
    """Consulta documental y preparación de borradores desde WF-00."""

    @abstractmethod
    def consultar_documento(self, documento_id: str) -> Mapping[str, object]:
        raise NotImplementedError

    @abstractmethod
    def crear_borrador(self, operacion: Mapping[str, object]) -> str:
        raise NotImplementedError


class Bold(ABC):
    """Consulta del estado de un pago; no confirma pagos por sí misma."""

    @abstractmethod
    def consultar_pago(self, referencia: str) -> Mapping[str, object]:
        raise NotImplementedError


class Drive(ABC):
    """Lectura de archivos autorizados; ADR-003 prevé Composio como puente."""

    @abstractmethod
    def leer_archivo(self, archivo_id: str) -> bytes:
        raise NotImplementedError


class Telegram(ABC):
    """Alertas sin datos personales, emitidas desde WF-00."""

    @abstractmethod
    def enviar_alerta(self, operacion: Mapping[str, object]) -> str:
        raise NotImplementedError
