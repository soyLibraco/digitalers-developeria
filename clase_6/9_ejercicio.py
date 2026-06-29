###
# A partir del código anterior, crea un método llamado "dejar_de_llover"
# que cambien el valor del atributo/variable de instancia a False
# y que imprima "Ha dejado de llover en la casa", pero si nunca llovió en esa casa,
# entonces mostrar "Nunca llovió en la casa"

class Casa:
    def __init__(self):  # método constructor
        self.lluvia = False  # variable de instancia / atributo
    def llover(self):  # método de instancia
        self.lluvia = True
        print("En esta casa empezó a llover")
    def dejar_de_llover(self):
        if self.lluvia:
            self.lluvia = False
            print("Ha dejado de llover en la casa.")
        else:
            print("Nunca llovió en la casa.")


def mostrar_estado(casa_1, casa_2):
    print(casa_1.lluvia)
    print(casa_2.lluvia)
    print()

def main():
    casa_1 = Casa()  # casa_1 es una instancia de la clase Casa
    casa_2 = Casa()  # casa_2 es una instancia de la clase Casa
    mostrar_estado(casa_1, casa_2)
    # casa_1.lluvia = True
    casa_1.llover()
    mostrar_estado(casa_1, casa_2)
    casa_1.dejar_de_llover()
    casa_2.dejar_de_llover()
    mostrar_estado(casa_1, casa_2)


main()