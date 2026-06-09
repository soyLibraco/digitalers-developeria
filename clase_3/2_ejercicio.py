###
# 1. Poner precio a cada producto y que se muestre en el menú.
# 2. Crear una billetera con saldo inicial (se puede usar input).
# 3. Al finalizar, mostrar el saldo final de la billetera.

# 4. Si el usuario elige un producto, restar el precio del producto al saldo inicial.
# 5. Si no tengo dinero suficiente, imprimir un mensaje.
# 6. Si se pudo realizar la compra, también, otro mensaje.
# # *******************************************************************************
# print("Menú de postres:")
# print("1. Flan")
# print("2. Helado")
# print("3. Tarta de manzana")
# postre = input("¿Qué postre quieres pedir? ")

# if postre == "1":
#     print("Pedido recibido: Flan")
# elif postre == "2":
#     print("Pedido recibido: Helado")
# elif postre == "3":
#     print("Pedido recibido: Tarta de manzana")
# else:
#     print(f"Lo solicitado ({postre}) no está en el menú")
# """

from time import sleep

precio_flan = 5
precio_helado = 3
precio_tarta = 8
saldo = float(input("¿Cuánto dinero tienes? "))

print("Menú de postres:")
print(f"1. Flan ${precio_flan}")
print(f"2. Helado ${precio_helado}")
print(f"3. Tarta de manzana ${precio_tarta}")
postre = input("¿Qué postre quieres pedir? ")

if postre == "1":
    if saldo >= precio_flan:
        print("Pedido recibido: Flan. Espera...")
        sleep(2)
        saldo = saldo - precio_flan
        print("✅ Compra realizada")
    else:
        print("✖️  No tienes dinero sufiente")
elif postre == "2":
    if saldo >= precio_helado:
        print("Pedido recibido: Helado. Espera...")
        sleep(2)
        saldo = saldo - precio_helado
        print("✅ Compra realizada")
    else:
        print("✖️  No tienes dinero sufiente")
elif postre == "3":
    if saldo >= precio_tarta:
        print("Pedido recibido: Tarta. Espera...")
        sleep(2)
        saldo = saldo - precio_tarta
        print("✅ Compra realizada")
    else:
        print("✖️  No tienes dinero sufiente")
else:
    print(f"Lo solicitado ({postre}) no está en el menú")