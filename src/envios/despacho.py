"""
Módulo de Envíos — ZHYRO
Gestión de costos de envío diferenciados por provincia y fecha
estimada de entrega, con cobertura a nivel nacional.
"""

from datetime import date, timedelta

TARIFAS = {
    "Lima": 10.00,
    "Callao": 12.00,
    "Arequipa": 18.00,
    "Cusco": 20.00,
    "Trujillo": 16.00,
    "Piura": 18.00,
}
TARIFA_OTRAS_PROVINCIAS = 25.00

DIAS_ENTREGA = {
    "Lima": 2,
    "Callao": 2,
}
DIAS_ENTREGA_PROVINCIA = 5

ENVIO_GRATIS_DESDE = 200.00


def costo_envio(provincia, monto_pedido=0.0):
    """Costo diferenciado por provincia. Los pedidos desde
    S/ 200.00 tienen envío gratuito a nivel nacional."""
    if not provincia or not provincia.strip():
        raise ValueError("Debe indicar la provincia de envío")
    if monto_pedido >= ENVIO_GRATIS_DESDE:
        return 0.00
    return TARIFAS.get(provincia.strip().title(), TARIFA_OTRAS_PROVINCIAS)


def fecha_estimada_entrega(provincia, fecha_compra=None):
    """Fecha estimada: 2 días hábiles Lima/Callao, 5 días resto del país."""
    base = fecha_compra or date.today()
    dias = DIAS_ENTREGA.get(provincia.strip().title(), DIAS_ENTREGA_PROVINCIA)
    return base + timedelta(days=dias)


def validar_direccion(direccion, distrito, provincia):
    """Una dirección de envío requiere los tres campos completos."""
    campos = [direccion, distrito, provincia]
    if any(c is None or not str(c).strip() for c in campos):
        raise ValueError("Dirección, distrito y provincia son obligatorios")
    return True
