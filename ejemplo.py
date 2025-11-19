import tkinter as tk
from tkinter import messagebox
def mostrar_mensaje():
    messagebox.showinfo("Aviso", "¡Botón presionado!")

ventana = tk.Tk()
ventana.title("Ventana simple")

label = tk.Label(ventana, text="Presiona el botón para ver un mensaje")
label.pack(pady=10)
boton = tk.Button(ventana, text="Haz click aquí", command=mostrar_mensaje)
boton.pack(pady=10)

ventana.mainloop()