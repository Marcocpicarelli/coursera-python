# Programa que calcula o fatorial de um valor n

n = int(input("Digite o valor de n: "))
contador = 1
fatorial = 1

if n < 0:
    print("0")

while contador <= n:
    fatorial = fatorial * contador
    contador = contador + 1
print(fatorial)
