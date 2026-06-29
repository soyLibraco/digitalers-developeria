"""
Objetivo: Hacer que el robot simula una acción.
Cada vez que ejecuta una, se le debe restar 20% de batería
Si la batería llega al 20% el robot no puede hacer ninguna tarea, y debe
mostrar un mensaje "Batería baja, debe recargar"
class Robot:
    def __init__(self):
        self.modelo = "X-1"
        self.bateria = 100
    def configurar_modelo(self):
        nuevo_modelo = input("Dame el nombre del modelo del robot: ")
        self.modelo = nuevo_modelo
        print(f"✅ Se actualizó el nombre del modelo a {self.modelo}")
mi_robot = Robot()
print(mi_robot.modelo)
print(mi_robot.bateria)
mi_robot.configurar_modelo()
"""

class Robot:
    def __init__(self):
        self.modelo = "X-1"
        self.bateria = 100
    def configurar_modelo(self):
        nuevo_modelo = input("Dame el nombre del modelo del robot: ")
        self.modelo = nuevo_modelo
        print(f"✅ Se actualizó el nombre del modelo a {self.modelo}")
    def accion(self):
        if self.bateria > 20:
            self.bateria -= 20
            print(f"Acción realizada. Batería restante: {self.bateria}%")
        else:
            print("Batería baja, se necesita recargar.")
        
mi_robot = Robot()
print(mi_robot.modelo)
print(mi_robot.bateria)
mi_robot.configurar_modelo()
mi_robot.accion()
mi_robot.accion()
mi_robot.accion()
mi_robot.accion()
mi_robot.accion()


##########################################################################


# class Robot:
#     def __init__(self):
#         self.modelo = "X-1"
#         self.bateria = 100

#     def configurar_modelo(self):
#         nuevo_modelo = input("Dame el nombre del modelo del robot: ")
#         self.modelo = nuevo_modelo
#         print(f"✅ Se actualizó el nombre del modelo a {self.modelo}")

#     def ejecutar_tarea(self):
#         if self.bateria >= 20:
#             print(f"🤖 '{self.modelo}': Ejecutando tarea... (Batería: %{self.bateria})")
#             self.bateria -= 20
#             print(f"🤖 '{self.modelo}': Fin de tarea. (Batería: %{self.bateria})")
#         else:
#             print(f"⚠️  Batería baja: recargar.")


# mi_robot = Robot()
# print(mi_robot.modelo)
# print(mi_robot.bateria)
# mi_robot.configurar_modelo()

# while mi_robot.bateria >= 20:
#     mi_robot.ejecutar_tarea()

# mi_robot.ejecutar_tarea()
# mi_robot.ejecutar_tarea()