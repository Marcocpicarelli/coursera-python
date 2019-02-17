total = int(input("Quantos números você deseja multiplicar? "))
           
produto = 1
valor = 1
contador = 0
            
while contador < total:
    valor = int(input("Digite um valor a ser multiplicado: "))
    produto = produto * valor
    contador = contador + 1

print("A multiplicação dos valores é " + str(produto) + ".")
