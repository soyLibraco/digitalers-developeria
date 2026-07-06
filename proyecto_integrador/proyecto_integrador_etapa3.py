###
# Etapa 3
# 
# La lista de alumnos creada en el módulo anterior, ahora debe ser un diccionario, en donde las claves serán nombres de alumnos
# y los valores sus respectivas cantidades de cursos.
#
# Para esto se debe modificar el código de las opciones 1 y 2 (agregar un nuevo alumno y ver la lista de alumnos).
#
# La tercera opción será "Ver la cantidad de cursos de un alumno". Deberá solicitar el nombre de un alumno e imprimir en pantalla
# el número de cursos que tiene asociados como clave.
# La cuarta opción es la de salir, como en la versión anterior.

usuario = input("\nIngrese su nombre de usuario: ")
password = input("\nIngrese su contraseña: ")
alumnos = {}
if usuario == "admin" and password == "uni123":
    opcion = 0
    while opcion != 4:
        print("\n--- MENU ---")
        print("\n1 - Añadir alumno a la lista.")
        print("2 - Ver la lista de alumnos.")
        print("3 - Ver la cantidad de cursos de un alumno.")
        print("4 - Salir.")
        opcion = int(input("\nIngrese una opción: "))
        if opcion == 1:
            nombre_alumno = input("\nIngrese el nombre del alumno: ").capitalize()
            cantidad_cursos = int(input("\nIngrese la cantidad de cursos: "))
            if nombre_alumno in alumnos:
                print(f"\nEl alumno {nombre_alumno} ya se encuentra inscripto con {alumnos[nombre_alumno]} cursos.")
            elif nombre_alumno.strip() != "" and cantidad_cursos > 0:
                alumnos[nombre_alumno] = cantidad_cursos
                print("\n¡El alumno fue añadido a la lista!")
            else:
                print("\nLos datos ingresados son incorrectos.")
        elif opcion == 2:
            if not alumnos:
                print("\nLa lista está vacía.")
            else:
                print("\n--- Lista de alumnos ---")
                for nombre, cursos in alumnos.items():
                    print(f"\nAlumno: {nombre} - Cursos: {cursos}")
        elif opcion == 3:
            nombre_alumno = input("\n Ingrese el nombre del alumno: ").capitalize()
            if nombre_alumno in alumnos:
                print(f"\nEl alumno {nombre_alumno} tiene {alumnos[nombre_alumno]} cursos.")
            else:
                print(f"\nEl alumno {nombre_alumno} no se encuentra inscripto.")
        elif opcion == 4:
            print("\n¡Gracias por utilizar el programa!")
        else:
            print("\nLa opción ingresada no es correcta, vuelva a intentarlo.")
            
else:
    print("\nUsuario y/o contraseña incorrecta.")