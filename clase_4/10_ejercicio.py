###
# Crear una función que imprima un apellido en mayúsculas, seguido de una coma, un espacio y el nombre de la persona
# con el primer caracter en mayúsculas y el resto en minúsculas.
#
# Crear una lista de nombres de personas y usar la función para ver la lista.

def crear_lista():
    nombres = []
    for i in range(3):
        nombre = input("Ingrese un nombre: ").capitalize()
        apellido = input("Ingrese un apellido: ").upper()
        nombres.append([apellido, nombre])
    return nombres


def imprimir_nombres():
    lista = crear_lista()
    for persona in lista:
        print(f"{persona[0]}, {persona[1]}")
imprimir_nombres()

###

def imprimir_nombre_completo(nombre, apellido):
    nombre_completo = f"{apellido.upper()}, {nombre.capitalize()}"
    print(nombre_completo)

def obtener_datos():
    persona_1 = ["guido", "van Rossum"]
    persona_2 = ["james", "gosling"]
    persona_3 = ["dennis", "ritchie"]
    lista_personas = [persona_1, persona_2, persona_3]
    return lista_personas

def principal():
    lista_personas= obtener_datos()
    for persona in lista_personas:
        nombre, apellido = persona
        imprimir_nombre_completo(nombre, apellido)

principal()