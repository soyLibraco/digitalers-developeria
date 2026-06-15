"""
Pedir al usuario que ingrese una lista de 10 números
y luego ordenarla de menor a mayor sin usar función sort().
"""

lista = []

for x in range(10):
    número = int(input("Ingresa un número: "))
    lista.append(número)

# lista = [5, 9, 45, 10, -4, 0, 4, 5, 6, 7]

# 👇 Completar

lista_ordenada = []

while len(lista) > 0:
    menor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero

    lista_ordenada.append(menor)
    lista.remove(menor)
print(lista_ordenada)

# print()
# for i in range(10):
#     for j in range(0, 10 - i - 1):
#         print(lista[j], lista[j + 1])
#         input()
#         if lista[j] > lista[j + 1]:
#             temporal = lista[j]
#             lista[j] = lista[j + 1]
#             lista[j + 1] = temporal

# print(lista)