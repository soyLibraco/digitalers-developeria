###
# Diccionario <dict>
# Son una colección de pares clave-valor (key-value). Son mutables.

diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
print(diccionario)
print(len(diccionario))

print("nombre" in diccionario)
print("apellido" in diccionario)

# Leer
print(diccionario["ciudad"])

# Crear
diccionario["peso"] = 70

print(diccionario)

# Modificar
diccionario["peso"] += 5
print(diccionario)

# Eliminar
del diccionario["peso"]
print(diccionario)