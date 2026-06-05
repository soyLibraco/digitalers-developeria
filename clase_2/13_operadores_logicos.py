###
# Operadores lógicos
# and - or - not
#
#AND: ambas expresiones deben ser "verdaderas" para que el resultado sea "verdadero"

estoy_vivo = True
doy_clases = True

if estoy_vivo and doy_clases:
    print("Estoy vivo y dando clases.")
else:
    print("No estoy vivo o no estoy dando clases.")

# OR: Al menos una parte de la expresión debe ser "verdadera"
# para que el resultado de la operación lógica sea "verdadero"

cliente_1_trabaja = True
cliente_2_trabaja = False

print("¿Debo prestar dinero a algún cliente hoy día?")
if cliente_1_trabaja or cliente_2_trabaja:
    print("Sí, voy a prestar porque al menos uno trabaja.")
else:
    print("No, porque niguno trabaja.")

# NOT: invierte el valor lógico

estoy_en_casa = True
print("¿Estoy en casa?")

if not estoy_en_casa:
    print("No estoy en casa.")
else:
    print("Sí, estoy en casa.")