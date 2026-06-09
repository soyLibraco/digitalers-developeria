# Ejercicio:
# Crear un programa que muestre 3 postres como menú.
# El usuario debe escribir uno.
# Si el nombre coincide con el menú, imprimir Pedido recibido: <tal cosa>", de lo contrario, imprimir <tal cosa> no está en el menú"

# postre_1 = "flan"
# postre_2 = "panqueque"
# postre_3 = "helado"

# pedido_usuario = input("Ingrese su postre: ")

# if pedido_usuario == postre_1 or pedido_usuario == postre_2 or pedido_usuario == postre_3:
#     print(f"Pedido recibido: {pedido_usuario}")
# else:
#     print(f"{pedido_usuario} no está en el menú.")

print("Menú de postres:")
print("1. Flan")
print("2. Helado")
print("3. Panqueque")
postre = input("¿Qué postre quieres pedir? ")
if postre == "1":
    print("Pedido recibido: Flan")
elif postre == "2":
    print("Pedido recibido: Helado")
elif postre == "3":
    print("Pedido recibido: Panqueque")
else:
    print(f"Lo solicitado ({postre}) no está en el menú")