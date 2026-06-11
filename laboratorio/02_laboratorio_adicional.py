###
# Ejercicio 1
#
# 1. Crea un programa que permita ingresar dos cadenas vía la consola y las compare.
# Luego, debe imprimir un mensaje en caso de que sean iguales y otro en caso de que sean diferentes.
cadena_a = input("Ingrese una cadena: ")
cadena_b = input("Ingrese otra cadena: ")

if cadena_a == cadena_b:
    print("Las cadenas son iguales.")
else:
    print("Las cadenas son diferentes.")

###
# 2. Crea un programa que solicite el nombre de un alumno a través de la consola, y luego chequee que no esté vacío.
# En caso de estarlo, tiene que imprimir un mensaje de error;
# caso contrario, deberá imprimir un mensaje indicando que se ingresó correctamente.
nombre_alumno = input("Ingrese su nombre: ")

if nombre_alumno.strip() == "": 
    print("No ha ingresado su nombre.")
else:
    print("Nombre ingresado correctamente.")

###
# 3. Pedir la edad por teclado y comparar si es mayor o menor de edad.
# No olvidar de que para poder comparar el ingreso, debe ser convertido a int, ya que el usuario ingresa un número entero.
edad_usuario = int(input("Ingrese su edad: "))
if edad_usuario >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

###
# Ejercicio 2
# 1. Con un bucle while, incrementar una variable entera de uno en uno (desde 0 a 10 sin incluir).
# Mostrar por pantalla el resultado por vuelta.
incrementador = 0
while incrementador < 9:
    print(incrementador)
    incrementador += 1

###
# 2. Pedir por teclado el nombre de usuario. Si está vacío, volver a pedirlo hasta que ingrese un nombre. Luego, saludar al usuario
nombre_usuario = ""
while nombre_usuario.strip() == "":
    nombre_usuario = input("Ingrese su nombre de usuario: ")
print(f"Bienvenido {nombre_usuario}")

### 
# Ejercicio 3
# 1. Inserta entre Alejandro y Roberto a Paula, y luego agrega al final a Silvina.
# 2. Para finalizar, recorre la lista y muestra a todos los nombres por pantalla.
nombres = ["Susana", "Alejandro", "Roberto"]
nombres.insert(2, "Paula")
nombres.append("Silvina")

for nombre in nombres:
    print(nombre)

###
# Ejercicio 4
# 1. Recorre la lista con un bucle for.
nombres = ["Agustina", "Marisa", "Juan", "Osvaldo"]
for nombre in nombres:
    print(nombre)

###
# Ejercicio 5
# 1. Crea un programa que solicite una fila y una columna e imprima en pantalla el número en esa posición
# según la siguiente matriz: matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
# Un ejemplo de entrada y salida es el siguiente (los caracteres en azul son ingresados por el usuario):
# Fila: 1
# Columna: 2
# 6.4
# El resultado es 6.4 porque es el valor ubicado en matriz[1][2].
# El programa debe chequear que la fila y la columna tengan valores válidos. 
# En este caso, las únicas filas válidas son 0 y 1; las columnas, 0, 1 y 2. 
# Si alguno de los dos valores es inválido, debe mostrar un mensaje de error.
matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
fila = int(input("Ingrese una Fila: "))
columna = int(input("Ingrese una Columna: "))

if fila not in [0, 1]:
    print("Valor de Fila incorrecto.")
elif columna not in [0, 1, 2]:
    print("Valor de columna incorrecto.")
else:
    print(f"El numero en la fila {fila} y la columna {columna} es {matriz[fila][columna]}")

###
# Ejercicio 6
# 1. Realiza un programa que, ingresando la edad de una persona, determine si es menor, 
# mayor con edad laboral o jubilado (contemplando jubilado para ambos sexos a los 65 años).
edad_ingresada = int(input("Ingrese su edad: "))

if edad_ingresada < 0:
    print("Edad ingresada incorrecta.")
elif edad_ingresada < 18:
    print("Usted es menor de edad.")
elif edad_ingresada < 65:
    print("Usted es mayor con edad laboral.")
else:
    print("Usted es mayor jubilado.")

###
# 2. Se tiene la matriz: m = [[10, 50, 5], [20, 30, 70], [15, 45, 80]]
# Recórrela con 2 sentencias for para mostrar cada uno
# de los elementos que la componen.
matrices = [[10, 50, 5], [20, 30, 70], [15, 45, 80]]
for matriz in matrices:
    print("--")
    for m in matriz:
        print(m)

###
# Ejercicio 7
# Una agencia de viajes tiene un sistema de información para paquetes turísticos. 
# Realiza un programa que, al ingresar el paquete (solo la letra), 
# genere una descripción de lo que contiene cada “combo”.

paquete_elegido = input("Seleccione un paquete (A, B, C o D): ").lower().strip()

if paquete_elegido not in ["a", "b", "c", "d"]:
    print("Paquete seleccionado incorrecto.")
elif paquete_elegido == "a":
    print("Cancún 7 noches + aéreos: u$s 1200 por persona.")
elif paquete_elegido == "b":
    print("Miami 8 noches + aéreos + alquiler de auto: u$s 1500 por persona.")
elif paquete_elegido == "c":
    print("Bariloche 10 noches + aéreos + excursiones: u$s 1300 por persona.")
else:
    print("Río de Janeiro 10 noches + aéreos + excursiones: u$s 1400 por persona.")