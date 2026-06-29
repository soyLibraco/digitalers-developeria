###
# Crear una clase llamada Robot.
# En el método __init__ definir 2 variables de instancia:
# - modelo = "x-1"
# - batería = 100

# Fera de la clase crear un objeto llamado mi_robot.
# Imprimir en pantalla el modelo y su batería.

# Dentro de la clase Robot, crear el primer método de instancia llamado configurar_modelo.
# Este método va a pedirle al usuario, usando input, que introduzca el nombre del modelo para el robot.
# Guardar ese nombre en self.modelo y mostrar un mensaje de confirmación en la terminal.

class Robot:
    def __init__(self, modelo, bateria):
        self.modelo = modelo
        self.bateria = bateria

    def configurar_modelo(self):
        self.modelo = input("Ingrese el nombre del modelo: ")
        print("Modelo añadido correctamente.")


def main():
    mi_robot = Robot(None, 100)
    mi_robot.configurar_modelo()
    print(f"Modelo: {mi_robot.modelo} | Batería: {mi_robot.bateria}%")
main()


# class Robot:
#     def __init__(self):
#         self.modelo = "X-1"
#         self.bateria = 100
#     def configurar_modelo(self):
#         nuevo_modelo = input("Dame el nombre del modelo del robot: ")
#         self.modelo = nuevo_modelo
#         print(f"✅ Se actualizó el nombre del modelo a {self.modelo}")

# mi_robot = Robot()
# print(mi_robot.modelo)
# print(mi_robot.bateria)
# mi_robot.configurar_modelo()