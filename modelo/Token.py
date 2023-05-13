class Token:
    def __init__(self, palabra, categoria, indiceSgte):
        self.palabra = palabra
        self.categoria = categoria
        self.indiceSgte = indiceSgte

    def __repr__(self):
        return f"token(palabra'{self.palabra}', categoria='{self.categoria}',indice_siguiente='{self.indiceSgte})"
