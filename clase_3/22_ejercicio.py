"""
Usando while, recorrer la frase, y cuando encuentre la letra 'P' salir del bucle:

frase = (
    "La creciente popularidad del aprendizaje "
    "automático probablemente hará que Python sea el lenguaje líder en el futuro."
)

print(frase)
"""


frase = (
    "La creciente popularidad del aprendizaje "
    "automático probablemente hará que Python sea el lenguaje líder en el futuro."
)
index = 0
while index < len(frase):
    print(index, frase[index])
    if frase[index] == "P":
        print(f"'P' hallada en índice: {index}")
        break
    index += 1
print(frase)