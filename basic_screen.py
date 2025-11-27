import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Aviso", "¡Botón presionado!")

ventana = tk.Tk()
ventana.title("Ventana interactiva")

label = tk.Label(ventana, text="¡Hola!", bg="lightblue", fg="darkblue")
label.pack(pady=10)

boton = tk.Button(ventana, text="Haz clic", bg="yellow", fg="black", command=mostrar_mensaje)
boton.pack(pady=10)

ventana.mainloop()


