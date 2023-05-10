import tkinter as tk
from MyFirst.modelo.AnalizadorL import AnalizadorLexico
from MyFirst.controlador.Ventana import WindowAnalizador

# Crear objeto Tk
root = tk.Tk()

# Crear ventana de analizador léxico
ventana_analizador = WindowAnalizador(root)

# Iniciar loop de la aplicación
root.mainloop()
