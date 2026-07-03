"""Pruebas del Módulo de Envíos.
Casos trazados: CP-ZHYRO-060 a CP-ZHYRO-065."""
from datetime import date
import pytest
from src.envios.despacho import costo_envio, fecha_estimada_entrega, validar_direccion


def test_cp060_costo_lima():
    assert costo_envio("Lima", 100.00) == 10.00


def test_cp061_costo_provincia_no_listada():
    assert costo_envio("Loreto", 100.00) == 25.00


def test_cp062_envio_gratis_desde_200():
    assert costo_envio("Cusco", 200.00) == 0.00


def test_cp063_provincia_vacia():
    with pytest.raises(ValueError):
        costo_envio("   ", 100.00)


def test_cp064_fecha_estimada_lima_vs_provincia():
    compra = date(2026, 7, 1)
    assert fecha_estimada_entrega("Lima", compra) == date(2026, 7, 3)
    assert fecha_estimada_entrega("Arequipa", compra) == date(2026, 7, 6)


def test_cp065_direccion_incompleta():
    with pytest.raises(ValueError):
        validar_direccion("Av. Los Polos 123", "", "Lima")
    assert validar_direccion("Av. Los Polos 123", "Miraflores", "Lima") is True
