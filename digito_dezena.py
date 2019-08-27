# Programa que exibe o dígito da dezena de um número

def exibe_digito_dezena(x):
    dezena = x // 10 % 10
    return dezena

n = int(input("Digite um número inteiro: "))

print(exibe_digito_dezena(n))
