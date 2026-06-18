###
#  Ejercicio 1
# Escribe una función mostrar_estrellas(cantidad) que muestre tantos * como indica cantidad, comenzando con un *.

def mostrar_estrellas(cantidad):
    for i in range(1, cantidad + 1):
        print("*" * i)

mostrar_estrellas(7)

###
# Ejercicio 2
# Crea una función que tome 2 números como argumentos y retorne el resultado.
# Por ejemplo, el código: sumar(10, 30). Debe retornar: 40

def sumar(a, b):
    return a + b

print(sumar(10, 30))

###
# Ejercicio 3
# Crea una función rango(desde, hasta, intervalo) que retorne una lista de números, tal como la función incorporada range(), aunque según el intervalo especificado.
# Por ejemplo, el siguiente código:
'''
lista = rango(1, 10, 2)
print(lista)
'''
# Debe imprimir: [1, 3, 5, 7, 9], puesto que se genra una lista desde 1 hasta 10 con un intervalo de 2.

def rango(desde, hasta, intervalo):
    lista = []
    while desde < hasta:
        lista.append(desde)
        desde += intervalo
    return lista

lista = rango(1, 20, 2)
print(lista)

###
# Ejercicio 4
# Crea una función que devuelva Verdadero si una lista de elementos es palíndroma (se lee igual en un sentido que en otro.)
# En caso contrario, debe devolver Falso.
# Por ejemplo:
'''
es_palindromo([3, 2, 3]) -> True
es_palindromo(["m", 2, 2, "m"]) -> True
'''

def es_palindromo(lista):
    inicio = 0
    final = len(lista) - 1
    while inicio < final:
        if lista[inicio] != lista[final]:
            return False
        inicio += 1
        final -= 1
    return True

print(es_palindromo(["NEUQUEN"]))
print(es_palindromo([7, 4, 1, 4, 7]))
print(es_palindromo([0, 1, 2, 3, 2, 1, 1]))
print(es_palindromo(["B", "B", "G", "B", "B"]))