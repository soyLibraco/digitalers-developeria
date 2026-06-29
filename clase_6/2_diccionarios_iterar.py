productos_lacteos = [
    {"nombre": "leche", "precio": 1.5, "cantidad": 10},
    {"nombre": "queso", "precio": 3.5, "cantidad": 1},
    {"nombre": "yogur", "precio": 4.5, "cantidad": 0},
    {"nombre": "manteca", "precio": 0.5, "cantidad": 123},
]
for producto in productos_lacteos:
    for clave, valor in producto.items():
        if clave == "precio":
            valor = f"${valor:.2f}"
        print(f"{clave}: {valor}")
    print("--------------------------------")