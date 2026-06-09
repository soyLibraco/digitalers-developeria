intentos = [0, 1, 2, 3, 4, 5, 6, 7]
nueva_lista = []

for numero in intentos:
    entrada = input("Dame un entero: ")
    if entrada.isdecimal():
        nueva_lista.append(int(entrada))
    else:
        print("Error, no es un número")
        continue
        print("Debe ingresar otro número")

print(nueva_lista)