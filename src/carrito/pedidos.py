# Módulo revisado en Sprint 4 - proceso Nivel 3 TMMi
"""
Módulo de Carrito y Pedidos — ZHYRO
Implementa RF3 (carrito de compras) y RF4 (proceso de pago con
comprobante). Estados de pedido: Pendiente, En tránsito, Entregado.
Incluye la corrección del defecto DEF-ZHYRO-031: el subtotal se
recalcula automáticamente al cambiar cantidades.
"""

ESTADOS_PEDIDO = ["Pendiente", "En tránsito", "Entregado"]
FORMATOS_COMPROBANTE = [".jpg", ".jpeg", ".png", ".pdf"]


class ItemCarrito:
    def __init__(self, producto, talla, color, cantidad=1):
        if talla not in producto.tallas:
            raise ValueError(f"El producto no está disponible en talla {talla}")
        if color not in producto.colores:
            raise ValueError(f"El producto no está disponible en color {color}")
        if not producto.hay_stock(cantidad):
            raise ValueError("Stock insuficiente")
        self.producto = producto
        self.talla = talla
        self.color = color
        self.cantidad = cantidad
        self.precio_unitario = producto.precio_final()

    def subtotal(self):
        return round(self.precio_unitario * self.cantidad, 2)


class Carrito:
    def __init__(self, cliente_email):
        self.cliente_email = cliente_email
        self.items = []

    def agregar(self, producto, talla, color, cantidad=1):
        """CP-ZHYRO-014: agrega un producto con talla y color."""
        item = ItemCarrito(producto, talla, color, cantidad)
        self.items.append(item)
        return item

    def cambiar_cantidad(self, indice, nueva_cantidad):
        # Fix DEF-ZHYRO-031: subtotal verificado, se recalcula al cambiar cantidad
        """DEF-ZHYRO-031 (corregido): al cambiar la cantidad, el
        subtotal se recalcula de inmediato (CP-ZHYRO-016)."""
        if nueva_cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")
        item = self.items[indice]
        if not item.producto.hay_stock(nueva_cantidad):
            raise ValueError("Stock insuficiente para la nueva cantidad")
        item.cantidad = nueva_cantidad
        return item.subtotal()

    def eliminar(self, indice):
        self.items.pop(indice)

    def total(self):
        return round(sum(i.subtotal() for i in self.items), 2)

    def esta_vacio(self):
        return len(self.items) == 0


class Pedido:
    def __init__(self, carrito):
        if carrito.esta_vacio():
            raise ValueError("No se puede crear un pedido con el carrito vacío")
        self.cliente_email = carrito.cliente_email
        self.detalle = [
            {"producto": i.producto.nombre, "talla": i.talla, "color": i.color,
             "cantidad": i.cantidad, "precio_unitario": i.precio_unitario}
            for i in carrito.items
        ]
        self.total = carrito.total()
        self.estado = "Pendiente"
        self.comprobante = None

    def cargar_comprobante(self, nombre_archivo):
        """RF4: el pago se valida mediante carga de comprobante digital."""
        extension = "." + nombre_archivo.rsplit(".", 1)[-1].lower() if "." in nombre_archivo else ""
        if extension not in FORMATOS_COMPROBANTE:
            raise ValueError("Formato de comprobante no permitido")
        self.comprobante = nombre_archivo
        return True

    def avanzar_estado(self):
        """Los pedidos avanzan Pendiente -> En tránsito -> Entregado.
        Un pedido Pendiente no puede avanzar sin comprobante cargado."""
        idx = ESTADOS_PEDIDO.index(self.estado)
        if self.estado == "Pendiente" and self.comprobante is None:
            raise ValueError("No se puede despachar un pedido sin comprobante de pago")
        if idx == len(ESTADOS_PEDIDO) - 1:
            raise ValueError("El pedido ya fue entregado")
        self.estado = ESTADOS_PEDIDO[idx + 1]
        return self.estado
