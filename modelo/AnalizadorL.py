from typing import List
from modelo.Token import Token
from modelo.Categoria import Categoria

class AnalizadorLexico:
    def __init__(self, codigoFuente: str):
        self.codigoFuente = codigoFuente
        self.listaTokens = []

    def analizar(self):
        i = 0
        while i < len(self.codigoFuente):
            token = self.extraerSgteToken(i)
            if token is not None:
                self.listaTokens.append(token)
                i = token.getPosicionFinal()
            else:
                i += 1

    def extraerSgteToken(self, indice: int) -> Token:
        token = None
        token = self.extraerEntero(indice)
        if token is not None:
            return token

        # TODO llamar acá todos los métodos de extraer, extraerDecimal, extraerIdentificador, etc.

        token = self.extraerNoReconocido(indice)
        return token

    def extraerEntero(self, indice: int) -> Token:
        if indice >= len(self.codigoFuente):
            return None

        if self.codigoFuente[indice].isdigit():
            posicion = indice
            while indice < len(self.codigoFuente) and self.codigoFuente[indice].isdigit():
                indice += 1
            return Token(self.codigoFuente[posicion:indice], Categoria.ENTERO, indice)
        else:
            return None

    def extraerNoReconocido(self, indice: int) -> Token:
        if indice >= len(self.codigoFuente):
            return None
        return Token(self.codigoFuente[indice], Categoria.NO_RECONOCIDO, indice+1)

    def getListaTokens(self) -> List[Token]:
        return self.listaTokens
