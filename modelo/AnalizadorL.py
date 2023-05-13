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

    def extraerSgteToken(self, indice):
        # se llama desde aqui a todos los métodos de extraer, extraerDecimal, extraerIdentificador, etc.

        token = self.extraer_operador_relacional(indice)
        if token is not None:
            return token

        token = self.extraer_operador_logico(indice)
        if token is not None:
            return token

        token = self.extraerEntero(indice)
        if token is not None:
            return token

        token = self.extraerNaturales(indice)
        if token is not None:
            return token

        token = self.extraerReales(indice)
        if token is not None:
            return token

        token = self.extraerIdentificador(indice)
        if token is not None:
            return token

        token = self.extraerPalabraReservada(indice)
        if token is not None:
            return token

        token = self.extraerOperadorAsignacion(indice)
        if token is not None:
            return token

        token = self.extraerOperadorIncrementoDecremento(indice)
        if token is not None:
            return token

        token = self.extraerSeparadorComa(indice)
        if token is not None:
            return token

        token = self.extraerTerminal(indice)
        if token is not None:
            return token

        token = self.extraerParentesisApertura(indice)
        if token is not None:
            return token

        token = self.extraerParentesisCierre(indice)
        if token is not None:
            return token

        token = self.extraerLlavesApertura(indice)
        if token is not None:
            return token

        token = self.extraerLlavesCierre(indice)
        if token is not None:
            return token

        token = self.extraer_hexadecimal(indice)
        if token is not None:
            return token

        token = self.extraer_cadena_caracteres(indice)
        if token is not None:
            return token

        token = self.extraerNoReconocido(indice)
        return token

    def extraerEntero(self, indice) -> Token:
        if indice >= len(self.codigoFuente):
            return None
        if self.codigoFuente[indice].isdigit():
            posicion = indice
            while indice < len(self.codigoFuente) and self.codigoFuente[indice].isdigit():
                indice += 1
            return Token(self.codigoFuente[posicion:indice], Categoria.ENTERO, indice)
        else:
            return None

    def extraerNaturales(self, indice) -> Token:
        if indice >= len(self.codigoFuente):
            return None

        if self.codigoFuente[indice].isdigit():
            posicion = indice
            while indice < len(self.codigoFuente) and self.codigoFuente[indice].isdigit():
                indice += 1
            numero = int(self.codigoFuente[posicion:indice])
            if numero >= 0:
                return Token(str(numero), Categoria.NATURAL, indice)
        return None

    def extraerReales(self, indice) -> Token:
        if indice >= len(self.codigoFuente):
            return None

        if self.codigoFuente[indice].isdigit():
            posicion = indice
            while indice < len(self.codigoFuente) and (
                    self.codigoFuente[indice].isdigit() or self.codigoFuente[indice] == '.'):
                indice += 1
            if self.codigoFuente[indice - 1] == '.':
                return None
            return Token(self.codigoFuente[posicion:indice], Categoria.REAL, indice)
        else:
            return None

    def extraerIdentificador(self, indice) -> Token:
        if indice >= len(self.codigoFuente):
            return None

        if self.codigoFuente[indice].isalpha():
            posicion = indice
            limite = min(indice + 10, len(self.codigoFuente))
            while indice < limite and (self.codigoFuente[indice].isalnum() or self.codigoFuente[indice] == '_'):
                indice += 1
            return Token(self.codigoFuente[posicion:indice], Categoria.IDENTIFICADOR, indice)
        else:
            return None

    def extraer_operador_relacional(self, indice):
        operadores_relacionales = ["==", "!=", "<", ">", "<=", ">="]
        for operador in operadores_relacionales:
            if self.codigoFuente.startswith(operador, indice):
                return Token(operador, Categoria.OPERADOR_RELACIONAL, indice + len(operador))
        return None

    def extraer_operador_logico(self, indice):
        operadores_logicos = ["&&", "||", "!"]
        for operador in operadores_logicos:
            if self.codigoFuente.startswith(operador, indice):
                return Token(operador, Categoria.OPERADOR_LOGICO, indice + len(operador))
        return None

    def extraerPalabraReservada(self, indice: int) -> Token:
        posicion = indice
        if indice >= len(self.codigoFuente):
            return None

        palabras_reservadas = ['if', 'else', 'for', 'while', 'switch', 'case', 'return', 'protected', 'static', 'class',
                               'int', 'float', 'bool', 'integer', 'double', 'String']

        for palabra in palabras_reservadas:
            if palabra in self.codigoFuente:
                indice = self.codigoFuente.find(palabra)
                return Token(self.codigoFuente[posicion:indice], Categoria.PALABRA_RESERVADA, indice, palabra)

        return None

    def extraerOperadorAsignacion(self, indice):
        operadores_asignacion = ['=', '+=', '-=', '*=', '/=', '%=', '**=', '&=', '|=', '^=', '<<=', '>>=', '//=']
        for operador in operadores_asignacion:
            if self.codigoFuente.startswith(operador, indice):
                return Token(operador, Categoria.OPERADOR_ASIGNACION, indice + len(operador))
        return None

    def extraerOperadorIncrementoDecremento(self, indice: int) -> Token:
        if indice < 0 or indice >= len(self.codigoFuente):
            return None

        peradorIncrementoDecremento = ['++', '--']

        for operador in peradorIncrementoDecremento:
            if self.codigoFuente.startswith(operador, indice):
                return Token(operador, Categoria.OPERADOR_INCREMENTO_DECREMENTO, indice + len(operador))

        return None

    def extraerSeparadorComa(self, indice: int) -> Token:
        if indice < 0 or indice >= len(self.codigoFuente):
            return None

        separadorComa = [',']

        for operador in separadorComa:
            if self.codigoFuente.startswith(operador, indice):
                return Token(operador, Categoria.SEPARADOR_COMA, indice + len(operador))

        return None

    def extraerTerminal(self, indice: int) -> Token:
        if indice < 0 or indice >= len(self.codigoFuente):
            return None

        separadorComa = [';']

        for operador in separadorComa:
            if self.codigoFuente.startswith(operador, indice):
                return Token(operador, Categoria.FIN_DE_SENTENCIA, indice + len(operador))

        return None

    def extraerParentesisApertura(self, indice: int) -> Token:
        if indice < 0 or indice >= len(self.codigoFuente):
            return None

        buscar = '('

        if self.codigoFuente[indice] == buscar:
            return Token(self.codigoFuente[indice], Categoria.PARENTESIS_APERTURA, indice + 1)

        return None

    def extraerParentesisCierre(self, indice: int) -> Token:
        if indice < 0 or indice >= len(self.codigoFuente):
            return None

        buscar = ')'

        if self.codigoFuente[indice] == buscar:
            return Token(self.codigoFuente[indice], Categoria.PARENTESIS_CIERRE, indice + 1)

        return None

    def extraerLlavesApertura(self, indice: int) -> Token:
        if indice < 0 or indice >= len(self.codigoFuente):
            return None

        buscar = '{'

        if self.codigoFuente[indice] == buscar:
            return Token(self.codigoFuente[indice], Categoria.LLAVES_APERTURA, indice + 1)

        return None

    def extraerLlavesCierre(self, indice: int) -> Token:
        if indice < 0 or indice >= len(self.codigoFuente):
            return None

        buscar = '}'

        if self.codigoFuente[indice] == buscar:
            return Token(self.codigoFuente[indice], Categoria.LLAVES_CIERRE, indice + 1)

        return None

    def extraer_hexadecimal(self, indice):
        if indice < 0 or indice >= len(self.codigoFuente):
            return None
        if self.codigoFuente[indice] == '#' and indice < len(self.codigoFuente) - 1:
            posicion = indice + 1
            while posicion < len(self.codigoFuente) and self.codigoFuente[posicion] in '0123456789abcdefABCDEF':
                posicion += 1
            return Token(self.codigoFuente[indice:posicion], Categoria.NUMERO_HEX, posicion)
        return None

    def extraer_cadena_caracteres(self, indice):
        if indice >= len(self.codigoFuente) or self.codigoFuente[indice] != "@":
            return None

        inicio = indice + 1
        fin = self.codigoFuente.find("@", inicio)
        if fin == -1:
            # No se encontró el cierre de la cadena
            fin = len(self.codigoFuente)

        return Token(self.codigoFuente[inicio:fin], Categoria.CADENA_CARACTERES, fin + 1)

    def extraerNoReconocido(self, indice: int):
        return Token(self.codigoFuente[indice], Categoria.NO_RECONOCIDO, indice + 1)

    def getListaTokens(self):
        return self.listaTokens
