# Programa que soma os algarismos de um número

n = int(input("Digite o número que você quer somar os dígitos: "))

soma = 0

while n >= 10:
    resto = n % 10 # Pega o último dígito do número
    n = n // 10 # Tira o último dígito do número
    soma = soma + resto # Soma o último dígito

soma = soma + n
print("A soma dos dígitos do seu número é " + str(soma) + ".")
