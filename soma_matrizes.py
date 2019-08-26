def soma_matrizes(m1, m2):
    linhas_m1 = len(m1)
    linhas_m2 = len(m2)
    colunas_m1 = len(m1[0])
    colunas_m2 = len(m2[0])
    if linhas_m1 != linhas_m2 or colunas_m1 != colunas_m2:
        return False
    else:
        nova_matriz = []
        for i in range(linhas_m1): # Percorre as linhas da matriz
            linha = []
            for j in range(colunas_m1): # Percorre colunas da matriz
                soma = m1[i][j] + m2[i][j]
                linha.append(soma)
            nova_matriz.append(linha)
        return nova_matriz
