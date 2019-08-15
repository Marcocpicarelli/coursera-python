def imprime_matriz(matriz):
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])

    cont_linha = 0
    cont_coluna = 0

    while cont_linha < num_linhas:
        while cont_coluna < num_colunas:
            print(matriz[cont_linha][cont_coluna], end = "")
            cont_coluna = cont_coluna + 1
        cont_coluna = 0
        print()
        cont_linha = cont_linha + 1

minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz)
