"""
Usar tkinter.
Crear una ventana. Título: "Ventana de inicio"
Configurar dimensiones
Ejecutar bucle
Usar una funcion main para instanciar la clase Tk
"""
import tkinter as tk

def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Ventana de inicio")
    ventana.config(width=720, height=480)
    ventana.mainloop()

def main():
    crear_ventana()

main()