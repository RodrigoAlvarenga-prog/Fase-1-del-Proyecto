"""
inventario.py
--------------
Funciones propias del sistema de inventario de una ferretería.

Cada función resuelve una sola tarea y retorna un valor útil.
Ninguna función queda aislada: se conectan entre sí y con main.py
para formar el flujo completo del sistema (registrar -> validar ->
actualizar -> consultar -> reportar).
"""


def calcularValorTotal(precio, cantidad):
    """
    Calcula el valor monetario total de un producto en inventario.

    Parámetros:
        precio (float): precio unitario del producto.
        cantidad (int): unidades disponibles.

    Retorna:
        float: precio * cantidad, redondeado a 2 decimales.
    """
    return round(precio * cantidad, 2)


def validarStockMinimo(cantidad, minimo=5):
    """
    Determina si un producto está por debajo del stock mínimo permitido.

    Parámetros:
        cantidad (int): unidades actuales del producto.
        minimo (int): umbral de stock bajo (por defecto 5).

    Retorna:
        bool: True si el stock está bajo (cantidad < minimo), False si no.
    """
    return cantidad < minimo


def registrarProducto(codigo, nombre, categoria, precio, cantidad, inventario):
    """
    Registra un nuevo producto en el inventario, calculando su valor
    total y verificando si ya nace con stock bajo.

    Usa calcularValorTotal() y validarStockMinimo() internamente:
    sus resultados se guardan como parte del registro del producto.

    Parámetros:
        codigo (str): identificador único del producto (ej. 'HR-001').
        nombre (str): nombre del producto.
        categoria (str): categoría (ej. 'Herramientas', 'Pintura').
        precio (float): precio unitario.
        cantidad (int): unidades iniciales.
        inventario (list): lista de diccionarios donde se almacena el inventario.

    Retorna:
        list: el inventario actualizado con el nuevo producto agregado.
    """
    valor_total = calcularValorTotal(precio, cantidad)
    stock_bajo = validarStockMinimo(cantidad)

    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "cantidad": cantidad,
        "valor_total": valor_total,
        "stock_bajo": stock_bajo,
    }
    inventario.append(producto)
    return inventario


def actualizarStock(codigo, cambio, inventario):
    """
    Actualiza la cantidad disponible de un producto existente (entrada
    o salida de mercadería) y recalcula su valor total y su estado
    de stock bajo.

    Recorre el inventario buscando el producto por código (repetición)
    y usa una decisión para evitar que la cantidad quede negativa.

    Parámetros:
        codigo (str): código del producto a actualizar.
        cambio (int): unidades a sumar (positivo) o restar (negativo).
        inventario (list): lista de diccionarios del inventario.

    Retorna:
        bool: True si el producto fue encontrado y actualizado,
              False si el código no existe en el inventario.
    """
    for producto in inventario:
        if producto["codigo"] == codigo:
            nueva_cantidad = producto["cantidad"] + cambio
            if nueva_cantidad < 0:
                nueva_cantidad = 0  # no se permite stock negativo
            producto["cantidad"] = nueva_cantidad
            producto["valor_total"] = calcularValorTotal(producto["precio"], nueva_cantidad)
            producto["stock_bajo"] = validarStockMinimo(nueva_cantidad)
            return True
    return False


def buscarProductoPorCodigo(codigo, inventario):
    """
    Busca un producto específico dentro del inventario por su código.

    Parámetros:
        codigo (str): código del producto a buscar.
        inventario (list): lista de diccionarios del inventario.

    Retorna:
        dict: el producto encontrado, o None si no existe.
    """
    for producto in inventario:
        if producto["codigo"] == codigo:
            return producto
    return None


def generarReporteInventario(inventario):
    """
    Genera un resumen del estado general del inventario: valor total
    de la mercadería y lista de productos con stock bajo.

    Parámetros:
        inventario (list): lista de diccionarios del inventario.

    Retorna:
        dict: {
            "valor_total_inventario": float,
            "productos_stock_bajo": list[str]  (nombres de productos)
        }
    """
    valor_total_inventario = 0
    productos_stock_bajo = []

    for producto in inventario:
        valor_total_inventario += producto["valor_total"]
        if producto["stock_bajo"]:
            productos_stock_bajo.append(producto["nombre"])

    return {
        "valor_total_inventario": round(valor_total_inventario, 2),
        "productos_stock_bajo": productos_stock_bajo,
    }
