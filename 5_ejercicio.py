"""
Consigna: Crear un programa que solicite el nombre
y el apellido
Devolver un saludo con de la siguiente forma:
Bienvenido <apellido>, <nombre>
"""

nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")

print("Bienvenido", apellido + ",", nombre)
print(f"Bienvenido {apellido}, {nombre}.")