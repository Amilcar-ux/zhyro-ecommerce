"""Pruebas del Módulo de Catálogo (RF1, RU1).
Casos trazados: CP-ZHYRO-001 a CP-ZHYRO-008."""
import pytest
from src.catalogo.productos import Producto, filtrar_productos, obtener_best_sellers


@pytest.fixture
def catalogo():
    return [
        Producto("Polo Oversize Negro", 59.90, 20, ["S", "M", "L"], ["Negro", "Blanco"], best_seller=True),
        Producto("Polera Esencial", 89.90, 10, ["M", "L", "XL"], ["Gris"]),
        Producto("Polo Básico", 39.90, 50, ["XS", "S", "M"], ["Blanco", "Azul"],
                 en_promocion=True, descuento_pct=20),
    ]


def test_cp001_producto_valido(catalogo):
    p = catalogo[0]
    assert p.nombre == "Polo Oversize Negro"
    assert p.hay_stock()


def test_cp002_precio_invalido():
    with pytest.raises(ValueError):
        Producto("Polo", 0, 10, ["M"], ["Negro"])


def test_cp003_talla_invalida():
    with pytest.raises(ValueError):
        Producto("Polo", 50, 10, ["XXXL"], ["Negro"])


def test_cp004_precio_final_con_promocion(catalogo):
    assert catalogo[2].precio_final() == 31.92


def test_cp005_descuento_fuera_de_rango():
    with pytest.raises(ValueError):
        Producto("Polo", 50, 10, ["M"], ["Negro"], en_promocion=True, descuento_pct=90)


def test_cp006_filtro_por_talla(catalogo):
    resultado = filtrar_productos(catalogo, talla="XL")
    assert [p.nombre for p in resultado] == ["Polera Esencial"]


def test_cp007_filtro_combinado_color_precio(catalogo):
    resultado = filtrar_productos(catalogo, color="Blanco", precio_max=40.00)
    assert [p.nombre for p in resultado] == ["Polo Básico"]


def test_cp008_filtro_excluye_inactivos(catalogo):
    catalogo[0].activo = False
    resultado = filtrar_productos(catalogo, talla="M")
    assert "Polo Oversize Negro" not in [p.nombre for p in resultado]


def test_best_sellers(catalogo):
    assert [p.nombre for p in obtener_best_sellers(catalogo)] == ["Polo Oversize Negro"]
