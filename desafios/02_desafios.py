###
# Ejercicio 1
# Crea un programa para estudiantes que cumpla con esta tarea: cada alumno debe ingresar su nota y, 
# de acuerdo con eso, el sistema debe mostrar un mensaje que diga:
# ● “Excelente” si la nota es un 10.
# ● “Muy bien” si está entre 7 y 9.
# ● “Bien” si está entre un 4 y un 6.
# ● “Mal” si está entre 0 y 3.
# ● Si la nota no corresponde a ninguno de estos valores, mostrar “La nota ingresada es incorrecta”.

nota = int(input("Ingrese su nota: "))
if nota == 10:
    print("Excelente")
elif nota >= 7:
    print("Muy bien")
elif nota >= 4:
    print("Bien")
elif nota >= 0:
    print("Mal")
else:
    print("La nota ingresada es incorrecta")

###
# Ejercicio 2
# Desarrolla un programa que cumpla los siguientes pasos:
# 1. Se preguntará el tipo de rol que desempeña una persona en una institución por una entrada del tipo input. 
# Los valores posibles son “admin” o “profesor”.
# 2. Luego, si la persona es “admin” o “profesor”, se debería pedir la contraseña, siendo la única válida “1234” (la contraseña se toma como string).
# 3. Si la contraseña ingresada es válida, se pedirá el nombre de la persona, y si no es vacío, se la saludará.
# Contemplar los casos donde no se cumple como corresponde y mostrar un mensaje en pantalla.

rol = input("Ingrese su rol (admin o profesor): ")
if rol in ["admin", "profesor"]:
    contraseña = input("Ingrese su contraseña: ")
    if contraseña == "1234":
        nombre = input("Ingrese su nombre: ")
        if nombre != "":
            print(f"Hola {nombre}")
        else:
            print("El nombre no puede estar vacío.")
    else:
        print("Contraseña incorrecta.")
else:
    print("Rol ingresado incorrecto.")

###
# Ejercicio 3
# 1. Lee la siguiente situación problemática:
# Un empleado cobró 300 dólares por mes desde enero a junio, 500 dólares de julio a octubre, y 700 dólares por mes en noviembre y en diciembre.
# 2. Crea un programa que calcule el sueldo promedio y que indique si este empleado está cobrando un sueldo bajo, normal o mejor de lo normal.
# ● Sueldo bajo: por debajo de 300 dólares.
# ● Sueldo normal: entre 300 a 900.
# ● Sueldo mejor de lo normal: más de 900 dólares.

enero_junio = 300 * 6
julio_octubre = 500 * 4
nomviembre_diciembre = 700 * 2

total = enero_junio + julio_octubre + nomviembre_diciembre
promedio = total / 12

if promedio < 300:
    print("Sueldo bajo")
elif promedio <= 900:
    print("Sueldo normal")
else:
    print("Sueldo mejor de lo normal")

# ###
# # Ejercicio 4
# # Programa para calcular si un año es bisiesto o no.

año = int(input("Ingrese un año: "))
if año % 400 == 0:
    print(f"{año} es un año bisiesto.")
elif año % 100 == 0:
    print(f"{año} no es un año bisiesto.")
elif año % 4 == 0:
    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto.")

###
# Ejercicio 5
# Escribe un programa que permita crear una lista de nombres.
# Para ello, el programa debe pedir un número y luego solicitar esa cantidad de nombres para crear la lista.
# Por último, el programa tiene que mostrar la lista creada.

cantidad_nombres = int(input("Ingrese la cantidad de nombres que quiere añadir a la lista: "))
lista_nombres = []

for i in range(cantidad_nombres):
    nombre = input("Ingrese un nombre: ")
    lista_nombres.append(nombre)
print(lista_nombres)
