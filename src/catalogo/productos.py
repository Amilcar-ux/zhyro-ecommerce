"""
Módulo de Catálogo de Productos — ZHYRO
Implementa RF1 (catálogo con precios y descripciones) y
RU1 (búsqueda por filtros de talla, color y precio).
"""

TALLAS_VALIDAS = ["XS", "S", "M", "L", "XL"]


class Producto:
    def __init__(self, nombre, precio, stock, tallas, colores,
                 coleccion="General", best_seller=False, en_promocion=False,
                 descuento_pct=0):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")
        for t in tallas:
            if t not in TALLAS_VALIDAS:
                raise ValueError(f"Talla inválida: {t}")
        if en_promocion and not (0 < descuento_pct <= 70):
            raise ValueError("El descuento en promoción debe estar entre 1% y 70%")
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.tallas = list(tallas)
        self.colores = list(colores)
        self.coleccion = coleccion
        self.best_seller = best_seller
        self.en_promocion = en_promocion
        self.descuento_pct = descuento_pct
        self.activo = True

    def precio_final(self):
        """Precio con descuento aplicado si está en promoción."""
        if self.en_promocion:
            return round(self.precio * (1 - self.descuento_pct / 100), 2)
        return self.precio

    def hay_stock(self, cantidad=1):
        return self.activo and self.stock >= cantidad


def filtrar_productos(productos, talla=None, color=None,
                      precio_min=None, precio_max=None):
    """RU1: filtra el catálogo por talla, color y rango de precio.

    Solo devuelve productos activos. Los filtros son acumulativos.
    """
    resultado = [p for p in productos if p.activo]
    if talla is not None:
        resultado = [p for p in resultado if talla in p.tallas]
    if color is not None:
        resultado = [p for p in resultado if color in p.colores]
    if precio_min is not None:
        resultado = [p for p in resultado if p.precio_final() >= precio_min]
    if precio_max is not None:
        resultado = [p for p in resultado if p.precio_final() <= precio_max]
    return resultado


def obtener_best_sellers(productos):
    return [p for p in productos if p.activo and p.best_seller]
