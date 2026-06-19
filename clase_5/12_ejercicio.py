def obtener_datos():
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    return nombre, precio, cantidad


def crear_producto(nombre, precio, cantidad):
    return {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
    }


def mostrar_producto(producto):
    print(
        f"El producto {producto['nombre']} cuesta ${producto['precio']} "
        f"y su stock es {producto['cantidad']}."
    )


def main():
    nombre, precio, cantidad = obtener_datos()
    producto = crear_producto(nombre, precio, cantidad)
    mostrar_producto(producto)


main()