###
# Crea un programa que realice una suma, una resta, multiplicación y división,
# a partir de dos números ingresados por el usuario,
# y luego mostrar el resultado por pantalla.

numero_uno = float(input("Ingrese un número: "))
numero_dos = float(input("Ingrese el siguiente número: "))

suma = numero_uno + numero_dos
print(f"La suma entre {numero_uno} y {numero_dos} es {suma}")

resta = numero_uno - numero_dos
print(f"La resta entre {numero_uno} y {numero_dos} es {resta}")

multiplicacion = numero_uno * numero_dos
print(f"La multiplicación entre {numero_uno} y {numero_dos} es {multiplicacion}")

if numero_dos != 0:
    division = numero_uno / numero_dos
    print(f"La división entre {numero_uno} y {numero_dos} es {division}")
else:
    print("No se puede dividir por 0.")