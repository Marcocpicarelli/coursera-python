# Função que cria matriz com um único valor

def cria_matriz(num_linhas, num_colunas, valor):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(valor)
        matriz.append(linha)
    print(matriz)

    print()

    cont = 0
    while cont < len(matriz):
        print(matriz[cont])
        cont = cont + 1

    print()

    linha = 1
    while linha <= num_linhas:
        print(valor, end = " ")
        coluna = 2
        while coluna < num_colunas:
            if linha == 1 or linha <= num_linhas:
                print(valor, end = " ")
            coluna = coluna + 1
        print(valor)
        linha = linha + 1

# Função que cria matriz e pergunta qual o valor de cada elemento

def cria_matriz2(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]: "))
            linha.append(valor)
        matriz.append(linha)

    cont = 0
    while cont < len(matriz):
        print(matriz[cont])
        cont = cont + 1

# Função que verifica se matrizes são multiplicáveis

def sao_multiplicaveis(m1, m2):
    if len(m1[0]) == len(m2):
        return True
    else:
        return False

# Função que retorna a matriz fora da lista

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

# Função que retorna as dimensões de uma matriz

def dimensoes(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    print(str(linhas) + "X" + str(colunas))

# Função que soma matrizes

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

# Função que multiplica matrizes

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

