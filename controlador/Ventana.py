import tkinter as tk
from MyFirst.modelo.AnalizadorL import AnalizadorLexico
from MyFirst.modelo.Token import Token

class WindowAnalizador(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Analizador léxico")

        # Crear entrada de texto
        self.label_texto = tk.Label(self.master, text="Ingrese texto aquí")
        self.label_texto.grid(row=0, column=0)
        self.entry_texto = tk.Entry(self.master)
        self.entry_texto.grid(row=0, column=1)

        # Crear botón de análisis
        self.btn_analizar = tk.Button(self.master, text="Analizar", command=self.obtenerText)
        self.btn_analizar.grid(row=1, column=1, pady=10)

        # Crear cuadro de texto para mostrar resultado
        self.label_resultado = tk.Label(self.master, text="Resultado:")
        self.label_resultado.grid(row=2, column=0)
        self.text_resultado = tk.Text(self.master, height=10, width=50)
        self.text_resultado.grid(row=3, column=0, columnspan=2, padx=10)

    def obtenerText(self):
        # Obtener texto ingresado por el usuario
        codigo_fuente = self.entry_texto.get()

        # Crear objeto AnalizadorLexico y analizar el texto ingresado
        analizador = AnalizadorLexico(codigo_fuente)
        analizador.analizar()

        # Obtener lista de tokens
        lista_tokens = analizador.getListaTokens()

        # Limpiar cuadro de texto de resultado
        self.text_resultado.delete('1.0', tk.END)

        # Mostrar resultados en el cuadro de texto de resultado
        for token in lista_tokens:
            self.text_resultado.insert(tk.END, f"Tipo: {token.getCategoria()} - Valor: {token.getValor()}\n")
