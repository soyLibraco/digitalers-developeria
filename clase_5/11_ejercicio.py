###
# Solicitar al usuario datos sobre un producto:
# - nombre
# - precio
# - cantidad
# Guardar en un diccionario y mostrar en la consola: "El producto <> cuesta $<> y su stock es <>."

inventario = {}

inventario["nombre"] = input("Ingrese el nombre del artículo: ")
inventario["precio"] = float(input("Ingrese el precio del artículo: "))
inventario["cantidad"] = int(input("Ingrese su cantidad en stock: "))

print(f"El producto '{inventario["nombre"]}' cuesta ${inventario["precio"]} y su stock es de {inventario["cantidad"]} unidades.")

'''
print("*** Producto ***")
nombre = input("Nombre: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))
producto = {
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad,
}
print(
    f"El producto {producto['nombre']} cuesta ${producto['precio']} y su stock es {producto['cantidad']}."
)
'''