# Programa que conta os números pares e ímpares digitados pelo usuário

terminou = False

p = i = 0

while (not terminou):
    n = int(input("Digite um número ou zero para terminar: "))
    if n == 0:
        terminou = True
    else:
        if n % 2 == 0:
            p = p + 1
        else:
            i = i + 1

print("Você digitou " + str(p) + " números pares.")
print("Você digitou " + str(i) + " números ímpares.")
