###
# A partir de la siguiente función, crea una lista de nombres (sin inputs)
# y saludar a cada uno.


nombres = ["Juan", "Erica", "Agustín", "Florencia", "Marcos", "Belén", "Ramiro"]

# def dar_bienvenida(nombre):
#     print(f"Bienvenido a la fiesta, {nombre}!!!")

# for nombre in nombres:
#     dar_bienvenida(nombre)

def dar_bienvenida(lista_nombres):
    for nombre in lista_nombres:
        print(f"Bienvenido a la fiesta, {nombre}!!!")

dar_bienvenida(nombres)