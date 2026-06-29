class Casa:
    def __init__(self):            # método constructor
        self.lluvia = False        # variable de instancia / atributo

    def llover(self):              # método de instancia
        self.lluvia = True
        print("En esta casa comenzó a llover.")

    def dejar_de_llover(self):     # método de instancia
        pass

###########################################################

casa_1 = Casa() # casa_1 es una instancia de la clase Casa.
casa_2 = Casa() # casa_2 es una instancia de la clase Casa.

print(casa_1.lluvia)
print(casa_2.lluvia)
print()
#casa_1.lluvia = True
casa_1.llover()
print(casa_1.lluvia)
print(casa_2.lluvia)