"""
Desarrollar un programa en Python que gestione una lista de tareas.

Crear una función agregar_tarea(lista, tarea) que agregue una tarea a la lista.
Crear una función eliminar_tarea(lista, tarea) que elimine una tarea si existe.
Crear una función mostrar_tareas(lista) que imprima todas las tareas numeradas.
Crear una función buscar_tarea(lista, palabra) que devuelva True si alguna tarea contiene esa palabra (no hace falta coincidencia exacta).

El programa principal debe:
    - Iniciar con una lista vacía.
    - Agregar al menos 3 tareas.
    - Mostrar las tareas.
    - Buscar una palabra.
    - Eliminar una tarea.
Mostrar nuevamente la lista final.
"""

def agregar_tarea(lista, tarea):
    lista.append(tarea)
    print("✅ Tarea agregada.")

def eliminar_tarea(lista, tarea):
    if tarea in lista:
        lista.remove(tarea)
        return True
    return False


def mostrar_tareas(lista):
    for indice, tarea in enumerate(lista, start = 1):
        print(f"{indice}. {tarea}")

def buscar_tarea(lista, palabra):
    for tarea in lista:
        if palabra in tarea.lower():
            return True
    return False

def principal():
    tareas = []
    agregar_tarea(tareas, "Estudiar Python")
    agregar_tarea(tareas, "Estudiar Git")
    agregar_tarea(tareas, "Estudiar inglés")
    mostrar_tareas(tareas)
    palabra = input("Ingresar palabra de búsqueda de tareas: ").lower()
    print(buscar_tarea(tareas, palabra))

principal()

'''
def agregar_tarea(lista, tarea):
    lista.append(tarea)
    return True

def eliminar_tarea(lista, tarea):
    if tarea in lista:
        lista.remove(tarea)
        return True
    return False

def mostrar_tareas(lista):
    for indice, tarea in enumerate(lista, start=1):
        print(f"{indice}. {tarea}")

def buscar_tarea(lista, palabra):
    for tarea in lista:
        if palabra.lower() in tarea.lower():
            return True
    return False

def principal():
    tareas = []
    agregar_tarea(tareas, "Estudiar Python")
    agregar_tarea(tareas, "Estudiar Git")
    agregar_tarea(tareas, "Estudiar Inglés")
    mostrar_tareas(tareas)
    # Buscar
    palabra = input("\nBuscar palabra: ")
    if buscar_tarea(tareas, palabra):
        print("👌 Se encontró la palabra en la lista de tareas")
    else:
        print("😔 No está la palabra en la lista de tareas")
    # Eliminar
    tarea_eliminar = input("\nTarea a eliminar (texto exacto): ")
    if eliminar_tarea(tareas, tarea_eliminar):
        print("🔥 Tarea eliminada")
    else:
        print("😔 La tarea no está en la lista de tareas")
    mostrar_tareas(tareas)

principal()
'''