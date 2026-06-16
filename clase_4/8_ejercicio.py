###
# Crear una función que reciba una cadena y devolver la cadena convertida en mayúsculas. Mostrar el resultado fuera de la función.
# Si el resultado es una cadena vacía, mostrar un mensaje indicando que la cadena está vacía.
# De lo contrario, mostrar la cadena.

def mayus(cadena):
    return cadena.upper()
    
resultado = mayus("")
if resultado:
    print(resultado)
else:
    print("La cadena está vacía")

print(mayus(""))
print(mayus("a ver si esta cadena sale en mayúsculas..."))

###

def convertir_mayusculas(texto):
    return texto.upper()

def principal():
    entrada = input("Dime algo para convertir a mayúsculas: ")
    texto_convertido = convertir_mayusculas(entrada)
    if texto_convertido:
        print(texto_convertido)
    else:
        print("La cadena está vacía")

principal()