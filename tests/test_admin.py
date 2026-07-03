"""Pruebas del Módulo Administrativo (RF5, RF6).
Casos trazados: CP-ZHYRO-040 a CP-ZHYRO-045."""
import pytest
from src.usuarios.autenticacion import Usuario, ROL_ADMIN
from src.catalogo.productos import Producto
from src.admin.panel import PanelAdministrativo


@pytest.fixture
def admin():
    return Usuario("admin@zhyro.pe", "AdminZhyro1!", rol=ROL_ADMIN)


@pytest.fixture
def panel(admin):
    p = PanelAdministrativo(admin)
    p.registrar_producto(Producto("Polo Oversize Negro", 59.90, 3, ["M"], ["Negro"]))
    p.registrar_producto(Producto("Polera Esencial", 89.90, 25, ["L"], ["Gris"]))
    return p


def test_cp040_acceso_restringido_a_admin():
    cliente = Usuario("cliente@zhyro.pe", "Segura123!")
    with pytest.raises(PermissionError):
        PanelAdministrativo(cliente)


def test_cp041_registrar_producto(panel):
    assert len(panel.inventario) == 2


def test_cp042_eliminacion_logica(panel):
    panel.eliminar_producto("Polera Esencial")
    p = [x for x in panel.inventario if x.nombre == "Polera Esencial"][0]
    assert p.activo is False


def test_cp043_actualizar_stock(panel):
    assert panel.actualizar_stock("Polo Oversize Negro", 40) == 40
    with pytest.raises(ValueError):
        panel.actualizar_stock("Polo Oversize Negro", -1)


def test_cp044_producto_inexistente(panel):
    with pytest.raises(ValueError):
        panel.eliminar_producto("No Existe")


def test_cp045_alertas_stock_minimo(panel):
    """RF: control de inventario con alertas de stock mínimo (<= 5)."""
    assert panel.alertas_stock_minimo() == ["Polo Oversize Negro"]
    panel.actualizar_stock("Polo Oversize Negro", 100)
    assert panel.alertas_stock_minimo() == []
