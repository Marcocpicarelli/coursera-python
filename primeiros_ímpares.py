# Programa exibe os números ímpares a partir
# de zero na quantidade desejada pelo usuário

n = int(input("Digite o valor de n: "))

contador = 1
valor = 1

while contador <= n:
    print(valor)
    contador = contador + 1
    valor = valor + 2
