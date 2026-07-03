"""Pruebas del Módulo de Usuarios y Autenticación (RF2).
Casos trazados: CP-ZHYRO-020 a CP-ZHYRO-027."""
import pytest
from src.usuarios.autenticacion import (
    Usuario, ESTADO_BLOQUEADO, ESTADO_ACTIVO, ROL_ADMIN, ROL_CLIENTE
)


@pytest.fixture
def usuario():
    return Usuario("cliente@zhyro.pe", "Segura123!")


def test_cp020_registro_valido(usuario):
    assert usuario.estado == ESTADO_ACTIVO
    assert usuario.rol == ROL_CLIENTE


def test_cp021_email_invalido():
    with pytest.raises(ValueError):
        Usuario("correo-sin-arroba", "Segura123!")


def test_cp022_password_corta():
    with pytest.raises(ValueError):
        Usuario("cliente@zhyro.pe", "abc")


def test_cp023_login_exitoso(usuario):
    assert usuario.iniciar_sesion("Segura123!") is True
    assert usuario.intentos_fallidos == 0


def test_cp024_login_fallido_incrementa_contador(usuario):
    assert usuario.iniciar_sesion("incorrecta") is False
    assert usuario.intentos_fallidos == 1


def test_cp025_login_exitoso_reinicia_contador(usuario):
    usuario.iniciar_sesion("incorrecta")
    usuario.iniciar_sesion("Segura123!")
    assert usuario.intentos_fallidos == 0


def test_cp026_cuenta_inactiva_no_inicia_sesion(usuario):
    usuario.desactivar()
    assert usuario.iniciar_sesion("Segura123!") is False


def test_cp027_bloqueo_por_intentos_fallidos(usuario):
    """CP-ZHYRO-027: tras 3 intentos fallidos la cuenta se bloquea
    y no acepta ni la contraseña correcta."""
    for _ in range(3):
        usuario.iniciar_sesion("incorrecta")
    assert usuario.estado == ESTADO_BLOQUEADO
    assert usuario.iniciar_sesion("Segura123!") is False


def test_desbloqueo_solo_administrador(usuario):
    for _ in range(3):
        usuario.iniciar_sesion("incorrecta")
    with pytest.raises(PermissionError):
        usuario.desbloquear(ROL_CLIENTE)
    usuario.desbloquear(ROL_ADMIN)
    assert usuario.estado == ESTADO_ACTIVO
    assert usuario.iniciar_sesion("Segura123!") is True
