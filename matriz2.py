def cria_matriz(num_linhas, num_colunas):
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

def le_matriz():
    x = int(input("Quantas linhas terá a sua matriz? "))
    y = int(input("Quantas colunas terá a sua matriz? "))

    cria_matriz(2, 3)

le_matriz()

