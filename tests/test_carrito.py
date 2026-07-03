"""Pruebas del Módulo de Carrito y Pedidos (RF3, RF4).
Casos trazados: CP-ZHYRO-010 a CP-ZHYRO-018 y CP-ZHYRO-030 a 036.
Incluye la prueba de regresión del defecto DEF-ZHYRO-031."""
import pytest
from src.catalogo.productos import Producto
from src.carrito.pedidos import Carrito, Pedido


@pytest.fixture
def producto():
    return Producto("Polo Oversize Negro", 59.90, 10, ["S", "M", "L"], ["Negro", "Blanco"])


@pytest.fixture
def carrito(producto):
    c = Carrito("cliente@zhyro.pe")
    c.agregar(producto, "M", "Negro", 1)
    return c


def test_cp014_agregar_producto_talla_color(carrito):
    """CP-ZHYRO-014: el carrito registra unidad, talla, color y precio."""
    item = carrito.items[0]
    assert item.cantidad == 1
    assert item.talla == "M"
    assert item.color == "Negro"
    assert item.precio_unitario == 59.90
    assert carrito.total() == 59.90


def test_cp015_talla_no_disponible(producto):
    c = Carrito("cliente@zhyro.pe")
    with pytest.raises(ValueError):
        c.agregar(producto, "XL", "Negro")


def test_cp016_regresion_def031_subtotal_se_recalcula(carrito):
    """DEF-ZHYRO-031: al cambiar la cantidad, el subtotal debe
    recalcularse sin recargar (Issue #31, corregido en PR #34)."""
    nuevo_subtotal = carrito.cambiar_cantidad(0, 3)
    assert nuevo_subtotal == 179.70
    assert carrito.total() == 179.70


def test_cp017_stock_insuficiente(carrito):
    with pytest.raises(ValueError):
        carrito.cambiar_cantidad(0, 99)


def test_cp018_eliminar_item(carrito):
    carrito.eliminar(0)
    assert carrito.esta_vacio()


def test_cp030_pedido_desde_carrito(carrito):
    pedido = Pedido(carrito)
    assert pedido.estado == "Pendiente"
    assert pedido.total == 59.90
    assert pedido.detalle[0]["talla"] == "M"


def test_cp031_pedido_carrito_vacio():
    with pytest.raises(ValueError):
        Pedido(Carrito("cliente@zhyro.pe"))


def test_cp032_comprobante_formato_valido(carrito):
    pedido = Pedido(carrito)
    assert pedido.cargar_comprobante("yape_operacion_884.jpg") is True


def test_cp033_comprobante_formato_invalido(carrito):
    """Defecto histórico del Daily Scrum: problemas con formato de
    archivos. Se valida la extensión permitida."""
    pedido = Pedido(carrito)
    with pytest.raises(ValueError):
        pedido.cargar_comprobante("comprobante.exe")


def test_cp034_no_despacha_sin_comprobante(carrito):
    pedido = Pedido(carrito)
    with pytest.raises(ValueError):
        pedido.avanzar_estado()


def test_cp035_flujo_completo_estados(carrito):
    """Seguimiento: Pendiente -> En tránsito -> Entregado."""
    pedido = Pedido(carrito)
    pedido.cargar_comprobante("plin_990.png")
    assert pedido.avanzar_estado() == "En tránsito"
    assert pedido.avanzar_estado() == "Entregado"


def test_cp036_pedido_entregado_no_avanza(carrito):
    pedido = Pedido(carrito)
    pedido.cargar_comprobante("plin_990.png")
    pedido.avanzar_estado()
    pedido.avanzar_estado()
    with pytest.raises(ValueError):
        pedido.avanzar_estado()
