total = int(input("Quantos números você deseja somar? "))

contador = 0
soma = 0
valor = 1

while contador < total:
    valor = int(input("Digite um valor a ser somado: "))
    soma = soma + valor
    contador = contador + 1
    
print("A soma dos valores digitados é " + str(soma))
