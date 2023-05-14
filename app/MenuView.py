import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from MyFirst.controlador.menu import Ui_Form
from MyFirst.modelo.AnalizadorL import AnalizadorLexico


class VentanaPrincipal(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Instanciar la interfaz y configurarla
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Conectar señales y slots
        self.ui.btnProcesar.clicked.connect(self.analizar)

    def analizar(self):
        # Obtener la expresión del QLineEdit
        expresion = self.ui.txtExpresion.text()

        # Crear una instancia del analizador léxico
        analizador = AnalizadorLexico(expresion)
        analizador.analizar()

        # Obtener la lista de tokens generada por el analizador léxico
        lista_tokens = analizador.getListaTokens()

        # Mostrar los tokens en el QTextEdit de salida
        self.ui.txtRespuesta.clear()
        for token in lista_tokens:
            self.ui.txtRespuesta.append(str(token))




def main():
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
