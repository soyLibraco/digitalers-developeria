###
# Ejercicio 1
# Función para forzar el ingreso numérico.
# Crea una función que fuerce el ingreso sólo de números.
# - Debe recibir un número por argumento y verificar que este sea un número posible de convertir a int.
# - En caso contrario, volver a pedir el ingreso dentro de la función.
# - Debe retornar el valor convertido a int.

def convertir(valor):
    while valor.isdecimal() == False:
        print("Error")
        valor = input("Ingrese nuevamente: ")
    valor = int(valor)
    return valor

valor = input("Ingrese un número: ")
print(convertir(valor))

###
# Ejercicio 2
# Realizar una función llamada area_rectangulo que reciba la base y la altura por argumento y que devuelva el área del rectángulo.

def area_rectangulo(altura, base):
    area = base * altura
    return area

area = area_rectangulo(15, 3)

print(area)