# Programa que calcula o IMC do usuário

def calcula_imc(altura, peso):
    imc = peso / (altura*altura)
    return imc    

nome = input("Olá, qual seu nome? ")
print(nome + ", esse programa vai calcular o seu IMC.")
x = float(input("Por favor, digite a sua altura em metros: "))
y = float(input("Agora digite o seu peso: "))

print(calcula_imc(x, y))



