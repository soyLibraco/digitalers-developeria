###
# Dado el código más bajo, devolver diferentes mensajes.
# No usar elif, ni operadores lógicos (aún no lo hemos visto)
# edad < 0  -> "edad no válida"
# edad < 13 -> "eres niño"
# edad < 18 -> "eres adolescente"
# edad < 65 -> "eres adulto"
# de lo contrario -> "eres adulto mayor"
# **********************************
edad = int(input("Edad: "))
if edad < 0:
    mensaje = "Edad no válida."
else:
    if edad < 13:
        mensaje = "Eres niño."
    else:
        if edad < 18:
            mensaje = "Eres adolescente."
        else:
            if edad < 65:
                mensaje = "Eres adulto."
            else:
                mensaje = "Eres adulto mayor."
print(mensaje)