repuestos_auto = [
    "filtro de aceite",
    "pastillas de freno",
    "bujías",
    "batería",
    "amortiguadores",
    "correa de distribución",
    "radiador",
    "alternador",
    "embrague",
    "filtro de aire",
    ]

nuevo_repuesto = input("Nuevo repuesto: ")
repuestos_auto.append(nuevo_repuesto)
print(repuestos_auto)
repuestos_auto.remove("filtro de aceite")
print(repuestos_auto)