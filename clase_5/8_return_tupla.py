def devolver_datos():
    return "hola", 123, True

devolucion = devolver_datos()
print(devolucion[0])
print(devolucion[1])
print(devolucion[2])

cadena, entero, booleano = devolver_datos()

print(cadena)
print(entero)
print(booleano)