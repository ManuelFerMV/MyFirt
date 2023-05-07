import tkinter as tk


def analizar_texto():
    texto = entrada_texto.get()
    texto_mayus = texto.upper()
    salida_texto.config(state=tk.NORMAL)
    salida_texto.delete('1.0', tk.END)
    salida_texto.insert(tk.END, texto_mayus)
    salida_texto.config(state=tk.DISABLED)


# Crear ventana
ventana = tk.Tk()
label = tk.Label(ventana, text="Analizador Léxico",
                 font=("chill chill", 5), anchor="w", )
label.grid(row=0, column=0, padx=10, pady=10)
label.pack()


ventana.title("MyFirst")

# Crear cuadro de entrada de texto
entrada_texto = tk.Entry(ventana, width=50)
entrada_texto.pack(padx=10, pady=10)
#entrada_texto.grid(row=0, column=1, padx=10, pady=10)

# Crear botón de análisis de texto
btn_analizar = tk.Button(ventana, text="Analizar", command=analizar_texto)
btn_analizar.pack(padx=10, pady=5)

# Crear cuadro de salida de texto
salida_texto = tk.Text(ventana, width=50, height=10, state=tk.DISABLED)
salida_texto.pack(padx=10, pady=10)

# Iniciar bucle de eventos
ventana.mainloop()