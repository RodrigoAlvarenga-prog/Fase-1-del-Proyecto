# Sistema de Inventario – Ferretería (Fase 1)

## Qué hace el programa
Administra el inventario de una ferretería: permite registrar productos,
actualizar existencias (entradas y salidas), buscar un producto por su
código y generar un reporte general con el valor total del inventario
y los productos con stock bajo.

## Cómo ejecutarlo
1. Asegúrate de tener Python 3 instalado.
2. Coloca `inventario.py` y `main.py` en la misma carpeta.
3. Ejecuta:
   ```
   python main.py
   ```
4. El programa imprime en consola 4 casos de prueba: registro inicial,
   una venta, una compra a proveedor, y un intento con un código que no
   existe, seguidos del reporte general.

## Funciones (`inventario.py`)

### `calcularValorTotal(precio, cantidad)`
- **Parámetros:** `precio` (float), `cantidad` (int).
- **Retorna:** `float` — el valor total (precio × cantidad).

### `validarStockMinimo(cantidad, minimo=5)`
- **Parámetros:** `cantidad` (int), `minimo` (int, por defecto 5).
- **Retorna:** `bool` — `True` si el stock está por debajo del mínimo.

### `registrarProducto(codigo, nombre, categoria, precio, cantidad, inventario)`
- **Parámetros:** datos del producto y la lista `inventario` donde se guarda.
- Usa internamente `calcularValorTotal()` y `validarStockMinimo()`.
- **Retorna:** `list` — el inventario con el nuevo producto agregado.

### `actualizarStock(codigo, cambio, inventario)`
- **Parámetros:** `codigo` del producto, `cambio` (positivo = entrada,
  negativo = salida), y `inventario`.
- Recorre el inventario (repetición) y usa una decisión para no permitir
  stock negativo; recalcula valor total y estado de stock bajo.
- **Retorna:** `bool` — `True` si encontró y actualizó el producto,
  `False` si el código no existe.

### `buscarProductoPorCodigo(codigo, inventario)`
- **Parámetros:** `codigo` del producto, `inventario`.
- **Retorna:** `dict` con el producto, o `None` si no se encuentra.

### `generarReporteInventario(inventario)`
- **Parámetros:** `inventario`.
- Recorre todos los productos (repetición) sumando el valor total y
  detectando cuáles tienen stock bajo.
- **Retorna:** `dict` con `valor_total_inventario` y
  `productos_stock_bajo` (lista de nombres).

## Casos de prueba incluidos en `main.py`
1. Registro inicial de 3 productos distintos.
2. Venta (salida de stock) de un producto.
3. Compra a proveedor (entrada de stock) de otro producto.
4. Intento de actualizar un producto con un código inexistente
   (verifica el manejo de errores).

## Equipo – parte de código desarrollada por cada integrante
- **Ever Gomez** – implementó `calcularValorTotal()` y `validarStockMinimo()`.
- **Marco Afane** – implementó `registrarProducto()`.
- **Rodrigo Alvarenga** – implementó `actualizarStock()`.
- **Luis Mejia** – implementó `buscarProductoPorCodigo()` y `generarReporteInventario()`.
- **Moises Moran** – implementó `main.py`, diseñó los casos de prueba y escribió este README.

> Recuerda: la rúbrica exige que **cada integrante** tenga al menos un
> commit propio (con su usuario) que modifique código funcional del
> proyecto — no solo commits al README.
