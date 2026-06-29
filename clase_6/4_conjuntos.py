# Conjuntos <set>
# Son una colección de objetos únicos y desordenados

conjunto = {1, 23.34, "Hola", True, False, None, "a", "b", "a"}
print(conjunto)

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

interseccion = conjunto_a.intersection(conjunto_b) # conjunto_a & conjunto_b
print(interseccion)

lista = [1, 2, 3, 2, 1, 4, 3, 2, 4, 5, 1]
print("Lista original: ", lista)

conjunto_lista = set(lista)
print("Conjunto de la lista: ", conjunto_lista)