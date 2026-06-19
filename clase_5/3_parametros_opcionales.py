def verificar_tarea(tarea, completada=False):
    if completada:
        print(f"La tarea '{tarea}' está completada.")
    else:
        print(f"La tarea '{tarea}', NO está completada")

verificar_tarea("Estudiar Python")
verificar_tarea("Estudiar algoritmos", False)
verificar_tarea("Estudiar patrones de diseño", True)