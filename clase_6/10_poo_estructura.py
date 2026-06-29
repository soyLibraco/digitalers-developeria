from dataclasses import dataclass


@dataclass
class Usuario:
    nombre: str
    edad: int
    contraseña: str


juan = Usuario(nombre="Juan", edad=30, contraseña="juan123")
lucy = Usuario(nombre="Lucy", edad=20, contraseña="luci123")


print(f"Hola soy {juan.nombre} y tengo {juan.edad} años.")
print(f"Hola soy {lucy.nombre} y tengo {lucy.edad} años.")

usuarios = [juan, lucy]
for usuario in usuarios:
    usuario.edad += 1

print(f"Hola soy {juan.nombre} y tengo {juan.edad} años.")
print(f"Hola soy {lucy.nombre} y tengo {lucy.edad} años.")