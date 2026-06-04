###
# 1. Resuelve el siguiente problema utilizando las herramientas aprendidas en el módulo.
# Tomás rindió 3 exámenes y desea saber su promedio a partir de esta información:
# Muestra el promedio por pantalla.

nota_uno = 10
nota_dos = 6
nota_tres = 8

promedio = nota_uno + nota_dos + nota_tres / 3

print(promedio)

###
# Calcula los minutos que hay en una semana declarando variables.

hora = 60
dia = 24 * hora
semana = 7 * dia
print(f"1 Hora {hora}, 1 día {dia}, 1 semana {semana}")

###
# Una juguetería tiene mucho éxito en la venta de dos de sus productos: payasos y muñecas. Suele
# hacer ventas por correo y la empresa de logística les cobra por el peso de cada paquete, por lo que
# necesitan calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca, 75 g.
# Ejercicio 2
# Escribe un programa que:
# ● Solicite al usuario el número de payasos y muñecas vendidos en el último pedido.
# ● Calcule el peso total del paquete que será enviado.

payaso = 112
muñeca = 75
cantidad_payasos = int(input("¿Cuántos payasos? "))
cantidad_muñecas = int(input("¿Cuántas muñecas? "))
peso_total = (cantidad_payasos * payaso) + (cantidad_muñecas * muñeca)

print(f"Para {cantidad_payasos} payasos y {cantidad_muñecas} muñecas, el peso total es de {peso_total} gramos")
