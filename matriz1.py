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

x = int(input("Quantas linhas terá a sua matriz? "))
y = int(input("Quantas colunas terá a sua matriz? "))
z = int(input("Qual o valor de preenchimento da matriz? "))

cria_matriz(x, y, z)

