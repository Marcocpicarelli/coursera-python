# Função que mostra todas as tabuadas

def tabuada():

    linha = 1
    coluna = 1
    while linha <= 10:
        while coluna <= 10:
            resultado = linha * coluna
            print(str(linha) + " x " + str(coluna) + " = " + str(resultado))
            coluna = coluna + 1
        linha = linha + 1
        print()
        print()
        coluna = 1

if __name__ == "__main__":
    tabuada()
        
