# Programa que calcula o IMC do usuário

nome = input("Olá, qual seu nome? ")
altura = input(nome + ", esse programa vai calcular o seu IMC. Por favor, digite qual é a sua altura em metros: ")
altura = float(altura) # conversão de string para float
peso = input(nome + ", agora digite qual o seu peso: ")
peso = float(peso) # conversão de string para float
imc = peso / (altura*altura)
imc = str(imc)  # conversão de float para string
print(nome + ", o seu IMC é " + imc)
