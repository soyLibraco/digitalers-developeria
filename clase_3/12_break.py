# Cláusula de escape.

from time import sleep

lista_numeros = [0, 1, 2, 3, 4, 5, 6, 7]
for numero in lista_numeros:
    sleep(0.5)
    print(numero)
    if numero == 3:
        print("Lo encontré!")
        break