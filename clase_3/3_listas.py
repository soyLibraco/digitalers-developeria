# Listas / arrays

lista = ["Agustina", "Tomás", "Isabel", "Julián"]

print(lista)
print(len(lista))
print("Agustina" in lista)
print("Santiago" in lista)

julian = "Julián" in lista

if julian:
    print("Sí, está en la lista")
else:
    print("No, no está en la lista")

lista_vacia = []
print(lista_vacia)
long_lista_vacia = len(lista_vacia)
print(long_lista_vacia)