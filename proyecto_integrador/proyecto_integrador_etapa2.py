###
# Etapa 2
# Menú
# Continúa el desarrollo del código incluyendo estos requisitos:

# a. Para ingresar al menú, solicitar nombre de usuario y contraseña. Solo si el usuario es “admin” y la contraseña es “uni123”,
# se muestra el menú. De lo contrario, se indica “Usuario y/o contraseña incorrecta”.
# Ingrese nombre de usuario: admin
# Ingrese la contraseña: uni123

# b. Una vez ingresado, mostrar el siguiente menú:
# Ingrese el número de la operación que desea ejecutar:
# 1 - Añadir un alumno a la lista.
# 2 - Ver la lista de alumnos.
# 3 - Salir.
# El sistema debe pedir una opción infinitamente hasta que el usuario escriba “3”.

# Si se presiona 1, debe solicitar el nombre de un alumno y la cantidad de cursos en la que se encuentra inscripto.
# Estos dos valores deben almacenarse como una lista de dos elementos (el nombre y la cantidad de cursos como un número entero) en una lista de alumnos.
# ● Opción 1:
# Ingrese el nombre del alumno: Pablo
# Ingrese la cantidad de cursos: 3
# ¡El alumno fue añadido a la lista!

# Si se presiona, recorrer la lista de alumnos y mostrar por pantalla.
# ● Opción 2:
# Lista de alumnos:
# Pablo - 3 cursos

# Si presiona 3, saludar al usuario y salir del sistema.
# ● Opción 3:
# ¡Gracias por utilizar el programa!

# Si el usuario presiona cualquier otro número, se debe informar que la opción no es correcta y volver a mostrar el menú.
# ● Opción distinta de 1, 2 o 3:
# La opción ingresada no es correcta, vuelva a intentarlo.

usuario = input("\nIngrese su nombre de usuario: ")
password = input("\nIngrese su contraseña: ")
alumnos = []
if usuario == "admin" and password == "uni123":
    opcion = 0
    while opcion != 3:
        print("\n--- MENU ---")
        print("\n1 - Añadir alumno a la lista.")
        print("2 - Ver la lista de alumnos.")
        print("3 - Salir.")
        opcion = int(input("\nIngrese una opción: "))
        if opcion == 1:
            nombre_alumno = input("\nIngrese el nombre del alumno: ")
            cantidad_cursos = int(input("\nIngrese la cantidad de cursos: "))
            if nombre_alumno.strip() != "" and cantidad_cursos > 0:
                alumnos.append([nombre_alumno, cantidad_cursos])
                print("\n¡El alumno fue añadido a la lista!")
            else:
                print("\nLos datos ingresados son incorrectos.")
        elif opcion == 2:
            if len(alumnos) == 0:
                print("\nLa lista está vacía.")
            else:
                print("\n--- Lista de alumnos ---")
                for alumno in alumnos:
                    print(f"\nAlumno: {alumno[0]} - Cursos: {alumno[1]}")
        elif opcion == 3:
            print("\n¡Gracias por utilizar el programa!")
        else:
            print("\nLa opción ingresada no es correcta, vuelva a intentarlo.")
            
else:
    print("\nUsuario y/o contraseña incorrecta.")