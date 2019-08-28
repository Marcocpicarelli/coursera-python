# Função que desenha o contorno de uma forma

def desenha_contorno(altura, largura):
    escreve_linha = 1

    while escreve_linha <= altura:
        print("*", end = "")
        coluna = 2
        while coluna < largura: 
            if escreve_linha == 1 or escreve_linha == altura:
                print("*", end = "")
            else:
                print(end = " ")
            coluna = coluna + 1
        print("*")
        escreve_linha = escreve_linha + 1

# Função que desenha uma forma preenchida

def desenha_preenchida(altura, largura):
    escreve_linha = 1

    while escreve_linha <= altura:
        print("*", end = "")
        coluna = 2
        while coluna < largura: 
            if escreve_linha == 1 or escreve_linha <= altura:
                print("*", end = "")
            coluna = coluna + 1
        print("*")
        escreve_linha = escreve_linha + 1
