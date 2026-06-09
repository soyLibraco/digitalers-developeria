###
# Agregar un elemento a la lista con input, y quitar otro con input.
lenguajes_programacion = [
    "Python",
    "JavaScript",
    "Java",
    "C#",
    "C++",
    "Go",
    "Rust",
    "TypeScript",
    "Kotlin",
    "Swift"
]

print(lenguajes_programacion)
agregar = input("Qué lenguaje deseas agregar? ")
if agregar in lenguajes_programacion:
    print("❌ El lenguaje ya está en  la lista.")
else:
    lenguajes_programacion.append(agregar)
    print("✅ Lenguaje añadido.")
print(lenguajes_programacion)
quitar = input("Qué lenguaje deseas quitar? ")
if quitar in lenguajes_programacion:
    print(f"✅ El lenguaje {quitar} ha sido removido.")
    lenguajes_programacion.remove(quitar)
else:
    print("❌ El lenguaje no estaba en la lista.")
print(lenguajes_programacion)