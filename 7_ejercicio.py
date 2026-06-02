"""
Solicitar al usuario la cantidad de stock que comprará.
Mostrar en la terminal el nombre del artículo, el precio unitario, y el precio final.
"""

articulo = "Lápiz"
precio = 15
cantidad = int(input("Cuántos querés?: "))
precio_final = cantidad * precio

print(f"Compraste {cantidad} {articulo} a ${precio} cada uno, el total será de ${precio_final}.")