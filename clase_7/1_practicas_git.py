"""
Crear el juego piedra - papel o tijera contra la computadora
"""

# Hecho por BBG
# Año 2026

# import random

# def jugada_maquina():
#     """Selecciona aleatoriamente una jugada para la computadora.

#     Returns:
#         tuple: Una tupla con la lista de opciones válidas y la elección de la computadora.
#     """
#     opciones = ["piedra", "papel", "tijera"]
#     computadora = random.choice(opciones)
#     return opciones, computadora

# def jugada_usuario(opciones):
#     """Solicita la elección del usuario y valida la entrada.

#     Args:
#         opciones (list): Lista de opciones válidas para el juego.

#     Returns:
#         str: La elección del usuario normalizada en minúsculas.
#     """
#     while True:
#         jugador = input("Escribe tu elección. Piedra, papel o tijera: ").lower()
#         if jugador not in opciones:
#             print("Tu elección está mal escrita...")
#             continue    
#         return jugador

# def partida(jugador, computadora):
#     """Determina el resultado de una partida y lo imprime en pantalla.

#     Args:
#         jugador (str): La elección del jugador.
#         computadora (str): La elección de la computadora.
#     """
#     if jugador == computadora:
#         print("Empate!")
#     elif jugador == "piedra" and computadora == "tijera":
#         print("Ganaste!")
#     elif jugador == "papel" and computadora == "piedra":
#         print("Ganaste!")
#     elif jugador == "tijera" and computadora == "papel":
#         print("Ganaste!")
#     else:
#         print("Perdiste!")
    
# def main():
#     """Ejecuta el flujo principal del juego piedra, papel o tijera.

#     Genera la jugada de la computadora, pide la jugada del usuario, muestra
#     ambas elecciones y evalúa el resultado de la partida.
#     """
#     opciones, computadora = jugada_maquina()
#     jugador = jugada_usuario(opciones)
#     print(f"Tu elección: {jugador} | Computadora: {computadora}")
#     partida(jugador, computadora)

# main()

import random


class JuegoPiedraPapelTijera:
    def configurar(self):
        self.opciones = ["piedra", "papel", "tijera"]
        self.reglas_victoria = {
            "piedra": "tijera",
            "papel": "piedra",
            "tijera": "papel",
        }

    def obtener_eleccion_jugador(self):
        """Pedir y validar la elección del jugador."""
        while True:
            jugador = input("Piedra, papel o tijera: ").lower()
            if jugador not in self.opciones:
                print("✖️  Entrada inválida")
                continue
            self.jugador = jugador
            return

    def obtener_eleccion_computara(self):
        """Elegir aleatoriamente la opción de la computadora."""
        self.computadora = random.choice(self.opciones)

    def determinar_resultado(self):
        """Calcular el resultado del juego entre jugador y computadora."""
        if self.jugador == self.computadora:
            self.resultado = "✅ Empate"
            return

        if self.reglas_victoria[self.jugador] == self.computadora:
            self.resultado = "✅ Ganaste"
            return

        self.resultado = "😔 Perdiste"

    def mostrar_resultado(self):
        """Mostrar en pantalla las elecciones y el resultado."""
        print("Jugador:", self.jugador)
        print("Computadora:", self.computadora)
        print(self.resultado)

    def jugar(self):
        """Ejecutar una partida completa de piedra, papel o tijera."""
        self.configurar()
        self.obtener_eleccion_jugador()
        self.obtener_eleccion_computara()
        self.determinar_resultado()
        self.mostrar_resultado()


juego = JuegoPiedraPapelTijera()
juego.jugar()