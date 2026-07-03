"""
Módulo de Usuarios y Autenticación — ZHYRO
Implementa RF2: registro e inicio de sesión con control de intentos
fallidos y bloqueo de cuenta. Estados: Activo, Inactivo, Bloqueado.
"""

MAX_INTENTOS_FALLIDOS = 3

ESTADO_ACTIVO = "Activo"
ESTADO_INACTIVO = "Inactivo"
ESTADO_BLOQUEADO = "Bloqueado"

ROL_CLIENTE = "Cliente"
ROL_ADMIN = "Administrador"


class Usuario:
    def __init__(self, email, password, rol=ROL_CLIENTE):
        if not email or "@" not in email:
            raise ValueError("El email no tiene un formato válido")
        if not password or len(password) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        self.email = email
        self._password = password
        self.rol = rol
        self.estado = ESTADO_ACTIVO
        self.intentos_fallidos = 0

    def iniciar_sesion(self, password):
        """Devuelve True si el login es exitoso.

        Tras MAX_INTENTOS_FALLIDOS intentos incorrectos consecutivos,
        la cuenta pasa a estado Bloqueado y ya no acepta credenciales,
        aunque sean correctas (CP-ZHYRO-027).
        """
        if self.estado == ESTADO_BLOQUEADO:
            return False
        if self.estado == ESTADO_INACTIVO:
            return False
        if password == self._password:
            self.intentos_fallidos = 0
            return True
        self.intentos_fallidos += 1
        if self.intentos_fallidos >= MAX_INTENTOS_FALLIDOS:
            self.estado = ESTADO_BLOQUEADO
        return False

    def desbloquear(self, solicitante_rol):
        """Solo un Administrador puede desbloquear una cuenta."""
        if solicitante_rol != ROL_ADMIN:
            raise PermissionError("Solo un Administrador puede desbloquear cuentas")
        self.estado = ESTADO_ACTIVO
        self.intentos_fallidos = 0

    def desactivar(self):
        self.estado = ESTADO_INACTIVO

    def es_administrador(self):
        return self.rol == ROL_ADMIN
