# Iterar sobre la lista de lenguajes de programación y agregar un número antes de cada lenguaje.

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

contador = 0
for lenguaje in lenguajes_programacion:
    contador += 1
    print(f"{contador}. {lenguaje}")

print("--------------")
for indice, lenguaje in enumerate(lenguajes_programacion, start=1):
    print(f"{indice}. {lenguaje}")