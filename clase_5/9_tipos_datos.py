enteros: int = 10
decimales: float = 3.14
booleanos: bool = True
cadenas: str = "cadena"
listas: list = [1, 2, 3]
tuplas: tuple = (1, 2, 3)

tipos_datos = [enteros, decimales, booleanos, cadenas, listas, tuplas]

for tipo in tipos_datos:
    print(f"'{tipo}' es una instancia de {type(tipo)}")