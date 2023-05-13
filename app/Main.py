from MyFirst.modelo.AnalizadorL import AnalizadorLexico


def main():
    codigo_fuente = 'JBJH@Q311[]@#125'
    analizador = AnalizadorLexico(codigo_fuente)
    analizador.analizar()

    # Accede a la lista de tokens generada por el analizador léxico
    lista_tokens = analizador.getListaTokens()
    for token in lista_tokens:
        print(token)


if __name__ == "__main__":
    main()
