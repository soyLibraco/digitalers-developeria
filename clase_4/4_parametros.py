###
#

def dar_bienvenida(nombre):
    print(f"Te damos la bienvenida a este programa, {nombre}.")

def dar_despedida():
    print("Gracias por utilizar el programa, adiós!")

def saludar():
    dar_bienvenida(nombre)
    dar_despedida()

    
nombre = input("¿Cómo te llamas? ")
saludar()