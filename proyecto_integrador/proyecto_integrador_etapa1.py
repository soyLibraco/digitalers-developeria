###
# ¿Qué es el proyecto integrador?
# ● Es un proyecto que se desarrollará durante el curso.
# ● Permite reafirmar los conocimientos adquiridos.
# ● Los ejercicios se realizarán en la clase junto al profesor/a.

# ETAPA 1
# Una universidad desea crear un programa para contabilizar los cursos que tiene cada alumno.
# Para ello, se debe realizar primero una aplicación de consola donde solo puede manejar el usuario con
# nombre “admin” y contraseña “uni123”.
# Una vez ingresado al sistema, debe aparecer un menú de opciones para dar de alta nuevos alumnos con la
# cantidad de cursos, ver listados, ver cursos por alumnos.
# Para finalizar, el sistema se debe mostrar en una interfaz gráfica.

# Consigna
# Crea un programa que solicite el nombre de un alumno a través de la consola y la cantidad de cursos, y luego
# muestre por pantalla esa información.

nombre_alumno = input("Ingrese su nombre: ")
cantidad_cursos = int(input("Ingrese la cantidad de cursos: "))

print(f"{nombre_alumno} está inscripto en {cantidad_cursos}, cursos.")