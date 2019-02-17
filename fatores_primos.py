n = int(input("Digite um número inteiro maior do que 1: "))

fator = 2
multiplicidade = 0

while n <= 1:
    print("Número inválido! Tente novamente. ")
    print()
    n = int(input("Digite um número inteiro maior do que 1: "))

while n > 1:
    while n % fator == 0:
        multiplicidade = multiplicidade + 1
        n = n / fator
    if multiplicidade > 0:
        print("O fator " + str(fator) + " tem multiplicidade " + str(multiplicidade) + ".")
    fator = fator + 1
    multiplicidade = 0
