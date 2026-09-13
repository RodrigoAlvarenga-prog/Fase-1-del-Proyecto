# Fase-1-del-Proyecto
# Sistema de inventario para un restaurante

## ¿De qué trata el proyecto?

Nuestro proyecto consiste en hacer un programa sencillo para llevar el control de algunos productos que se utilizan en un restaurante.

La idea es poder registrar los productos que tenemos, saber cuánto cuestan, cuántas unidades hay disponibles y calcular cuánto vale en total la cantidad de cada producto.

También hicimos una opción para saber si hay poco producto disponible. Para nuestro programa consideramos que hay poco stock cuando quedan menos de 5 unidades.

## ¿Cómo funciona?

Al iniciar el programa ya tenemos algunos productos registrados para poder probar que el sistema funciona.

Los productos que usamos al inicio son:

- Carne: $5.00, 10 unidades
- Pan: $1.00, 20 unidades
- Queso: $2.00, 4 unidades

Después de iniciar el programa aparece un menú con tres opciones:

1. Mostrar inventario
2. Registrar producto
3. Salir

Si elegimos la primera opción, el programa muestra los productos que tenemos, su precio, cantidad, valor total y si tienen stock bajo o suficiente.

Si elegimos la segunda opción, podemos escribir los datos de un producto nuevo y agregarlo al inventario.

La tercera opción permite cerrar el programa.

## Funciones

Para organizar mejor el programa utilizamos varias funciones.

### calcularTotal(precio, cantidad)

Esta función sirve para calcular cuánto vale en total la cantidad de un producto.

Recibe el precio y la cantidad, los multiplica y devuelve el resultado.

Por ejemplo, si tenemos 10 productos que cuestan $5 cada uno, el resultado es $50.

### validarStock(cantidad)

Esta función sirve para revisar si queda poco producto.

Si la cantidad es menor que 5, el programa considera que el stock es bajo. Si hay 5 o más unidades, considera que el stock es suficiente.

La función devuelve `True` cuando el stock es bajo y `False` cuando es suficiente.

### registrarProducto(nombre, precio, cantidad, inventario)

Esta función sirve para agregar un producto nuevo al inventario.

Primero utiliza `calcularTotal()` para saber el valor total del producto y también utiliza `validarStock()` para saber si hay poco stock.

Después guarda los datos del producto en el inventario y devuelve el inventario actualizado.

### mostrarInventario(inventario)

Esta función sirve para mostrar todos los productos que tenemos registrados.

Utilizamos un ciclo `for` para ir mostrando cada producto uno por uno.

También revisamos el stock de cada producto para indicar si es bajo o suficiente.

## Pruebas

Para comprobar que el programa funciona utilizamos diferentes productos y cantidades.

### Prueba 1

Producto: Carne

Precio: $5.00

Cantidad: 10

Resultado:

- Total: $50.00
- Stock: Suficiente

### Prueba 2

Producto: Pan

Precio: $1.00

Cantidad: 20

Resultado:

- Total: $20.00
- Stock: Suficiente

### Prueba 3

Producto: Queso

Precio: $2.00

Cantidad: 4

Resultado:

- Total: $8.00
- Stock: Bajo

Con estas pruebas comprobamos tanto el cálculo del valor total como la parte que revisa el stock.

## Archivos del proyecto

El proyecto tiene tres archivos:

- `inventario.py`: aquí colocamos las funciones que utilizamos para trabajar con el inventario.
- `main.py`: aquí está el menú y la parte principal del programa.
- `README.md`: este archivo explica de qué trata el proyecto y cómo funciona.

## ¿Cómo ejecutar el programa?

Para utilizar el programa necesitamos tener Python y JupyterLab.

Los archivos `inventario.py` y `main.py` deben estar dentro de la misma carpeta.

Para iniciar el programa ejecutamos `main.py`.

## Integrantes

- Integrante 1: Rodrigo Alvarenga
- Integrante 2: Moises Moran
- Integrante 3: Luis Mejia
- Integrante 4: Marco Afane
- Integrante 5:Ever Gomez

def calcularTotal(precio, cantidad):
    total = precio * cantidad
    return total


def validarStock(cantidad):
    if cantidad < 5:
        stock_bajo = True
    else:
        stock_bajo = False

    return stock_bajo


def registrarProducto(nombre, precio, cantidad, inventario):
    total = calcularTotal(precio, cantidad)
    stock_bajo = validarStock(cantidad)

    producto = {
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad,
        'total': total,
        'stock_bajo': stock_bajo
    }

    inventario.append(producto)

    return inventario
