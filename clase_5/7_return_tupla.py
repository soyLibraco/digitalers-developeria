def operar(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

def main():
    # resultado = operar(10, 5)
    # suma, resta, multiplicacion, division = resultado
    suma, resta, multiplicacion, division = operar(10, 5)
    print(f"suma={suma}")
    print(f"{resta=}")
    print(f"{multiplicacion=}")
    print(f"{division=}")

main()