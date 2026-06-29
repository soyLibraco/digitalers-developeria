import tkinter as tk

def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Ventana de inicio")
    ventana.config(width=720, height=480)

    entrada = tk.Entry()
    entrada.place(x=300, y=100)

    boton = tk.Button(text="Click me")
    boton.place(x=350, y=150)

    ventana.mainloop()

def main():
    crear_ventana()

main()