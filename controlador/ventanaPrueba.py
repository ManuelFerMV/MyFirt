import tkinter as tk

# Función para analizar el texto y mostrarlo en mayúsculas
def analizar_texto():
    texto = entrada_texto.get("1.0", tk.END).strip() # Obtiene el texto del cuadro de entrada
    texto_mayusculas = texto.upper() # Convierte el texto a mayúsculas
    salida_texto.config(state=tk.NORMAL)
    salida_texto.delete('1.0', tk.END) # Limpia el cuadro de salida
    salida_texto.insert(tk.END, texto_mayusculas) # Muestra el texto en mayúsculas en el cuadro de salida
    #salida_texto.config(fg="red") # Cambia el color del texto
    salida_texto.config(state=tk.DISABLED)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Analizador Léxico")

ventana.configure(bg='#FFDBAC') # Cambia el color de fondo de la ventana

# Titulo
titulo = tk.Label(ventana, text="Analizador Léxico", font=("Chill Chill", 18), fg="sky blue", bg='#FFDBAC')
titulo.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Etiqueta y cuadro de entrada de texto
etiqueta_texto = tk.Label(ventana, text="Ingrese su texto:", fg="red", bg='#FFDBAC')
etiqueta_texto.grid(row=1, column=0, padx=10, pady=10)

entrada_texto = tk.Text(ventana, height=10, width=50, state="normal")
entrada_texto.grid(row=1, column=1, padx=10, pady=10)

# Botón para analizar el texto
boton_analizar = tk.Button(ventana, text="Analizar", command=analizar_texto, bg='white')
boton_analizar.grid(row=2, column=1, padx=10, pady=10)

# Cuadro de salida de texto
etiqueta_salida = tk.Label(ventana, text="Texto en mayúsculas:", fg="red", bg='#FFDBAC')
etiqueta_salida.grid(row=3, column=0, padx=10, pady=10)

salida_texto = tk.Text(ventana, height=10, width=50, state="disabled")
salida_texto.grid(row=3, column=1, padx=10, pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
