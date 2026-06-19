###
# Tupla: es una colección de objetos indexados, pero a diferencia de las listas, son inmutables.
# (no puedo agregar, modificar ni quitar elementos)
tupla = (1, 2, 3, 4, 5, "final")
print(tupla)
print(len(tupla))
print(tupla[0])
print(tupla[-1])
frutas = ("naranja", "manzana", "limón")
# n = frutas[0]
# m = frutas[1]
# l = frutas[2]
n, m, l = frutas
print(n, m, l)