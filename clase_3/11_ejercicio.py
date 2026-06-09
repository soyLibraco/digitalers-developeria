###
# A partir del siguiente código, si el número iterado es 3, entonces imprimir "lo encontré".

from time import sleep

lista_numeros = [0, 1, 2, 3, 4, 5]
for numero in lista_numeros:
    sleep(0.5)
    print(numero)
    if numero == 3:
        print("Lo encontré!")