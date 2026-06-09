"""
Sistema de alerta térmica
El sistema recibe una lista de lecturas de temperatura.
Procesar con las siguientes reglas:
1. Lecturas erróneas (continue): Si una temperatura es negativa (ej. -99) sería
un fallo del sensor. Mostrar mensaje de advertencia y saltar a la siguiente lectura
sin guardarla en la lista.
2. Alerta crítica (break): Si una temperatura es mayor o igual a 100, emitir una alarma
y detener el análisis
3. Lecturas válidas (append): Si la temperatura es normal, agregar a la nueva lista
# **************************
lecturas = [22, -26, -99, 24, 10, 105, 5, 10]
temperaturas_validas = []
"""

lecturas = [22, -26, -99, 24, 10, 105, 5, 10]
temperaturas_validas = []

for temperatura in lecturas:
    if temperatura < 0:
        print(f"{temperatura}°C Temperatura erronea.")
        continue
    elif temperatura >= 100:
            print(f"Atención! {temperatura}°C Temperatura demasiado alta.")
            break
    temperaturas_validas.append(temperatura)
print(temperaturas_validas)