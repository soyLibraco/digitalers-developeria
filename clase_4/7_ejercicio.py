###
# Crear una función llamada duplicar.
# Debe recibir un número(string) y devolverlo duplicado(entero).
# Otra que pregunte por el número a duplicar (input).
# debe devolver ese string.
#Crear una función principal que sea la que llame al resto.

# def pedir_numero():
#     numero = input("Ingrese un número: ")
#     print(numero)
#     return numero

# def duplicar(numero):
#     numero = int(numero)
#     duplicado = numero * 2
#     return duplicado

# def principal():
#     resultado = duplicar(pedir_numero())
#     print(resultado)

# principal()

###

def duplicar(numero):
    return numero * 2

def preguntar_numero():
    numero_str = input("Número: ")
    return numero_str

def principal():
    numero = int(preguntar_numero())
    numero_duplicado = duplicar(numero)
    print(numero_duplicado)

principal()