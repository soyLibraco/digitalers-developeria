dividendo_str = input("Dividendo: ")
divisor_str = input("Divisor: ")

dividendo = float(dividendo_str)  
divisor = float(divisor_str)           # Esto puede hacerse en la misma primer línea
                                       # aplicando float() al input

division = dividendo / divisor

print(f"El resultado de {dividendo} / {divisor} es {division}")


