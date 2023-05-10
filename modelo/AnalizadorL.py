from typing import List

from MyFirst.modelo.Categoria import Categoria
from MyFirst.modelo.Token import Token


class AnalizadorLexico:
    def __init__(self, codigoFuente):
        self.codigoFuente = codigoFuente
        self.listaTokens = []

    def analizar(self):
        i = 0
        while i < len(self.codigoFuente):
            if self.codigoFuente[i].isspace():
                i += 1
                continue

            token = self.extraerSgteToken(i)
            self.listaTokens.append(token)
            i = token.indiceSgte

    def extraerSgteToken(self, indice: int):

        token = self.extraerEntero(indice)
        if token is not None:
            return token

        # llamar acá todos los métodos de extraer, extraerDecimal, extraerIdentificador, etc.

        token = self.extraerNoReconocido(self, indice)
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

    def extraerOperadorAritmetico(self, indice: int, cadena=None) -> Token:

        posicion = indice
        self.codigoFuente = cadena
        if indice >= len(self.codigoFuente):
            return None

        operadores_aritmeticos = ['+', '-', '*', '/', '%', '**']

        if indice >= 0 and indice < len(cadena):
            if cadena[indice] in operadores_aritmeticos:
                return Token(self.codigoFuente[posicion:indice], Categoria.OPERADOR_ARITMETICO, indice)
        return None

    def extraerPalabraReservada(self, indice: int, cadena=None) -> Token:

        posicion = indice
        self.codigoFuente = cadena
        if indice >= len(self.codigoFuente):
            return None

        palabras_reservadas = ['if', 'else', 'for', 'while', 'switch', 'case', 'return', 'protected', 'static', 'class',
                               'int', 'float', 'bool', 'integer', 'double', 'String']

        for palabra in palabras_reservadas:
            if palabra in cadena:
                indice = cadena.find(palabra)
                return Token(self.codigoFuente[posicion:indice], Categoria.PALABRA_RESERVADA, indice, palabra)

        return None, -1

    def extraerOperadorIncremento(self, indice: int, cadena=None) -> Token:

        posicion = indice
        self.codigoFuente = cadena
        if indice >= len(self.codigoFuente):
            return None

        palabras_reservadas = ['++', '--']

        for palabra in palabras_reservadas:
            if palabra in cadena:
                indice = cadena.find(palabra)
                return palabra, indice
                return Token(self.codigoFuente[posicion:indice], Categoria.OPERADOR_ARITMETICO, indice, palabra)

        return None, -1

    def extraerParentesis(self, indice: int, cadena: str) -> Token:
        if indice >= len(cadena):
            return None

        parentesis = ['(', ')']

        for par in parentesis:
            if cadena[indice] == par:
                return Token(cadena[indice], Categoria.PARENTESIS, indice)

        return None

    def extraerLlave(self, indice: int, cadena: str) -> Token:
        if indice >= len(cadena):
            return None

        llaves = ['{', '}']

        for llave in llaves:
            if cadena[indice] == llave:
                return Token(llave, Categoria.LLAVE, indice)

        return None

    def extraerReales(self, indice: int, cadena=None) -> Token:
        def extraerReal(indice: int, cadena: str) -> Token:
            regex = r'\d+\.\d+'  # Expresión regular para números reales
            match = re.search(regex, cadena[indice:])  # Buscar la expresión regular en la cadena a partir del índice
            if match:
                inicio = match.start() + indice  # Obtener la posición inicial del número real en la cadena
                final = match.end() + indice  # Obtener la posición final del número real en la cadena
                return Token(cadena[inicio:final], Categoria.REAL, final)
            else:
                return None

    def extraerOperadorRelacional(self, indice: int, cadena: str) -> Token:
        if indice >= len(cadena):
            return None

        operadores_relacionales = ['<', '>', '<=', '>=', '==', '!=']

        for operador in operadores_relacionales:
            if cadena[indice:indice + len(operador)] == operador:
                return Token(cadena[indice:indice + len(operador)], Categoria.OPERADOR_RELACIONAL, indice)

        return None

    def extraerOperadorLogico(indice: int, cadena: str) -> Token:
        if indice >= len(cadena):
            return None

        operadores_logicos = ['and', 'or', 'not']

        for operador in operadores_logicos:
            if cadena[indice:indice + len(operador)] == operador:
                return Token(cadena[indice:indice + len(operador)], Categoria.OPERADOR_LOGICO, indice)

        return None

    def extraerOperadorAsignacion(indice: int, cadena: str) -> Token:
        if indice >= len(cadena):
            return None

        operadores_asignacion = ['=', '+=', '-=', '*=', '/=', '%=', '**=', '&=', '|=', '^=', '<<=', '>>=', '//=']

        for operador in operadores_asignacion:
            if cadena[indice:indice + len(operador)] == operador:
                return Token(cadena[indice:indice + len(operador)], Categoria.OPERADOR_ASIGNACION, indice)

        return None

    def extraerOperadorIncrementoDecremento(self, indice: int, cadena: str) -> Token:
        if indice >= len(cadena):
            return None

        operadores_incremento = ['++', '--']

        for operador in operadores_incremento:
            if cadena[indice:indice + len(operador)] == operador:
                return Token(cadena[indice:indice + len(operador)], Categoria.OPERADOR_INCREMENTO_DECREMENTO, indice)

        return None

    def extraerSeparadorComa(indice: int, cadena: str) -> Token:
        if indice >= len(cadena):
            return None

        if cadena[indice] == ',':
            return Token(',', Categoria.SEPARADOR_COMA, indice)

        return None

    def extraerFinDeSentencia(indice: int, cadena: str) -> Token:
        if indice >= len(cadena):
            return None

        if cadena[indice] == ';':
            return Token(';', Categoria.FIN_DE_SENTENCIA, indice)

        return None

    def extraerNumeroHexadecimal(self, indice: int, cadena: str) -> Token:
        if indice >= len(cadena):
            return None

        # Comprobamos si el primer carácter es un número hexadecimal
        if cadena[indice] not in '0123456789abcdefABCDEF':
            return None

        i = indice + 1
        while i < len(cadena) and cadena[i] in '0123456789abcdefABCDEF':
            i += 1

        return Token(cadena[indice:i], Categoria.NUMERO_HEX, indice)

    def extraerCadena(indice: int, cadena: str) -> Token:
        if indice >= len(cadena):
            return None

        if cadena[indice] != '"':
            return None

        i = indice + 1
        while i < len(cadena):
            if cadena[i] == '"':
                return Token(cadena[indice:i + 1], Categoria.CADENA, indice)
            i += 1

        return None

    def extraerComentario(indice: int, cadena: str) -> Token:
        if indice >= len(cadena):
            return None

        if cadena[indice:indice + 2] == '# ':
            # El comentario comienza con '# ' y termina en una nueva línea o al final de la cadena
            comentario = ""
            indice += 2
            while indice < len(cadena) and cadena[indice] != '\n':
                comentario += cadena[indice]
                indice += 1
            return Token('# ' + comentario, Categoria.COMENTARIO, indice)

        return None

    def extraerNoReconocido(self, indice: int) -> Token:
        if indice >= len(self.codigoFuente):
            return None
        return Token(self.codigoFuente[indice], Categoria.NO_RECONOCIDO, indice + 1)

    def getListaTokens(self) -> List[Token]:
        return self.listaTokens
