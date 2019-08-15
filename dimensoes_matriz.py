def dimensoes(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    print(str(linhas) + "X" + str(colunas))          

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[1], [2], [3]]

dimensoes(m1)
dimensoes(m2)
