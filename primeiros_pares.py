# Programa exibe os números pares a partir de
# zero na quantidade desejada pelo usuário

n = int(input("Digite o valor de n: "))

contador = 1
valor = 2

while contador <= n:
    print(valor)
    contador = contador + 1
    valor = valor + 2
