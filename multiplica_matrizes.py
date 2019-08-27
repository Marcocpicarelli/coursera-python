def multiplica_matrizes(a, b):

    linhas_a = len(a)
    linhas_b = len(b)
    colunas_a = len(a[0])
    colunas_b = len(b[0])

    assert linhas_a == colunas_b

    nova_matriz = []

    for linha in range(linhas_a): # Percorre as linhas da matriz
        nova_matriz.append([]) #Começando nova linha
        for coluna in range(colunas_b): # Percorre colunas da matriz
            nova_matriz[linha].append(0) # Adiciona nova coluna na linha
            for i in range(colunas_a):
                nova_matriz[linha][coluna] += a[linha][i] * b[i][coluna]
    return nova_matriz

if __name__ == "__main__":
    m1 = [[1, 2, 3],[4, 5, 6]]
    m2 = [[1, 2],[3, 4],[5, 6]]
    print(multiplica_matrizes(m1, m2))
