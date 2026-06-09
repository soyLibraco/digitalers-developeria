"""
Escribir la letra de la canción Me gusta de Manu Chao,
utilizando la sentencia de iteración for:
Deberán crear también una lista con los párrafos de la canción
para poder imprimirlos correctamente por pantalla.
https://www.letras.com/manu-chao/7352/
"""

estrofas = [
    ["Me gusta viajar, me gustas tú.",
    "Me gusta los aviones, me gustas tú.",
    "Me gusta la mañana, me gustas tú.",
    "Me gusta el viento, me gustas tú.",
    "Me gusta soñar, me gustas tú.",
    "Me gusta la mar, me gustas tú."],
    ["¿Qué voy a hacer? Je ne sais pas",
    "¿Qué voy a hacer? Je ne sais plus",
    "¿Qué voy a hacer? Je suis perdu",
    "¿Qué horas son, mi corazón?"],
    ["Me gusta la moto, me gustas tú.",
    "Me gusta correr, me gustas tú.",
    "Me gusta la lluvia, me gustas tú.",
    "Me gusta volver, me gustas tú.",
    "Me gusta marihuana, me gustas tú.",
    "Me gusta colombiana, me gustas tú.",
    "Me gusta la montaña, me gustas tú.",
    "Me gusta la noche, me gustas tú."],
    ["¿Qué voy a hacer? Je ne sais pas",
    "¿Qué voy a hacer? Je ne sais plus",
    "¿Qué voy a hacer? Je suis perdu",
    "¿Qué horas son, mi corazón?"],
    ["Me gusta la cena, me gustas tú.",
    "Me gusta la vecina, me gustas tú.",
    "Me gusta su cocina, me gustas tú.",
    "Me gusta camelar, me gustas tú.",
    "Me gusta la guitarra, me gustas tú.",
    "Me gusta el reggae, me gustas tú."],
    ["¿Qué voy a hacer? Je ne sais pas",
    "¿Qué voy a hacer? Je ne sais plus",
    "¿Qué voy a hacer? Je suis perdu",
    "¿Qué horas son, mi corazón?",
    "¿Qué voy a hacer? Je ne sais pas",
    "¿Qué voy a hacer? Je ne sais plus",
    "¿Qué voy a hacer? Je suis perdu",
    "¿Qué horas son, mi corazón?",
    "¿Qué voy a hacer? Je ne sais pas",
    "¿Qué voy a hacer? Je ne sais plus",
    "¿Qué voy a hacer? Je suis perdu",
    "¿Qué horas son, mi corazón?"]
]

for estrofa in estrofas:
    for frase in estrofa:
        print(frase)
    print()