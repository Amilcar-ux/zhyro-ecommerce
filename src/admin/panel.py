"""
Módulo Administrativo — ZHYRO
Implementa RF5 (gestión de productos) y control de inventario con
alertas de stock mínimo. Solo accesible para el rol Administrador.
"""

STOCK_MINIMO_DEFAULT = 5


class PanelAdministrativo:
    def __init__(self, usuario):
        if not usuario.es_administrador():
            raise PermissionError("Acceso restringido al rol Administrador")
        self.usuario = usuario
        self.inventario = []

    def registrar_producto(self, producto):
        """RF5: crear productos desde el panel."""
        self.inventario.append(producto)
        return len(self.inventario)

    def eliminar_producto(self, nombre):
        """RF5: la eliminación es lógica (el producto se desactiva),
        para no romper el historial de pedidos."""
        for p in self.inventario:
            if p.nombre == nombre:
                p.activo = False
                return True
        raise ValueError(f"Producto no encontrado: {nombre}")

    def actualizar_stock(self, nombre, nuevo_stock):
        if nuevo_stock < 0:
            raise ValueError("El stock no puede ser negativo")
        for p in self.inventario:
            if p.nombre == nombre:
                p.stock = nuevo_stock
                return p.stock
        raise ValueError(f"Producto no encontrado: {nombre}")

    def alertas_stock_minimo(self, umbral=STOCK_MINIMO_DEFAULT):
        """Control de inventario: lista los productos activos cuyo
        stock está en o por debajo del umbral."""
        return [p.nombre for p in self.inventario
                if p.activo and p.stock <= umbral]
