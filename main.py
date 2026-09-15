"""
main.py
--------
Programa principal del sistema de inventario de una ferretería.

Conecta todas las funciones de inventario.py en un flujo real:
registrar productos -> actualizar stock -> buscar -> generar reporte.

Incluye al menos 3 casos de prueba distintos, como pide la rúbrica.
"""

from inventario import (
    registrarProducto,
    actualizarStock,
    buscarProductoPorCodigo,
    generarReporteInventario,
)

inventario = []

# --- Registro inicial de productos ---
inventario = registrarProducto("HR-001", "Martillo", "Herramientas", 8.50, 12, inventario)
inventario = registrarProducto("HR-002", "Taladro", "Herramientas", 45.00, 3, inventario)
inventario = registrarProducto("PT-010", "Galón de pintura blanca", "Pintura", 15.75, 20, inventario)

print("=== Caso de prueba 1: inventario recién registrado ===")
for p in inventario:
    print(p)

# --- Caso 2: salida de mercadería (venta) ---
print("\n=== Caso de prueba 2: venta de 5 taladros ===")
actualizado = actualizarStock("HR-002", -5, inventario)
print("¿Se actualizó?", actualizado)
print(buscarProductoPorCodigo("HR-002", inventario))

# --- Caso 3: entrada de mercadería (compra a proveedor) ---
print("\n=== Caso de prueba 3: ingreso de 30 martillos ===")
actualizado = actualizarStock("HR-001", 30, inventario)
print("¿Se actualizó?", actualizado)
print(buscarProductoPorCodigo("HR-001", inventario))

# --- Caso 4: intento de actualizar un producto que no existe ---
print("\n=== Caso de prueba 4: código inexistente ===")
actualizado = actualizarStock("XX-999", 10, inventario)
print("¿Se actualizó?", actualizado)

# --- Reporte final ---
print("\n=== Reporte general del inventario ===")
reporte = generarReporteInventario(inventario)
print(reporte)
