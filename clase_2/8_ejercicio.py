###
# A partir del código 7_if_anidados.py
# hacer que el usuario tenga 4 posibilidades de adivinar.

PALABRA_SECRETA = "azul"            # Una variable en mayúsculas se considera 
                                    # que es una variable constante.

entrada_usuario = input("Adivina la palabra secreta: ")

if entrada_usuario == PALABRA_SECRETA:
    print("✨ Has adivinado")
else:
    entrada_usuario = input("Error.😔 Vuelve a intentar: ")
    if entrada_usuario == PALABRA_SECRETA:
        print("✨ Has adivinado")
    else:
        entrada_usuario = input("Error.😔 Vuelve a intentar: ")
        if entrada_usuario == PALABRA_SECRETA:
            print("✨ Has adivinado!")
        else:
            entrada_usuario = input("Error.😔 Vuelve a intentar: ")
            if entrada_usuario == PALABRA_SECRETA:
                print("✨ Has adivinado!")
            else:
                print("😔 Has perdido")
