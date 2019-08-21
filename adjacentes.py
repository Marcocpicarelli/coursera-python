def adjacentes(n):

    anterior = -1
    atual = -2
    adjacentes_iguais = False # Indicador de passagem

    while n > 0 and not adjacentes_iguais:
        atual = n % 10 # Pega o último dígito do número
        anterior = (n // 10) % 10 # Retira o último dígito do número e pega o anterior
        if atual == anterior:
            adjacentes_iguais = True
        n = n // 10 # Retira o último dígito do número

    if adjacentes_iguais:
        print("O número tem dois '" + str(atual) + "' como dígitos adjacentes iguais.")
    else:
        print("O número não possui dígitos adjacentes iguais.")
