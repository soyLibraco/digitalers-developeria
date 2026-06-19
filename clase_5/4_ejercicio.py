###
# Ejercicio con funciones con parámetros predeterminados.
# Crear una función dividir que reciba dos argumentos, uno opcional y otro obligatorio.
# Debe devolver el resultado de la división de ambos. Si se pasa un solo argumento, dividir / 1.

def dividir(numero_uno, numero_dos=1):
    resultado = numero_uno / numero_dos
    print(f"{numero_uno} / {numero_dos} = {resultado}")


dividir(5, 3)
dividir(7)
dividir(24, 4)