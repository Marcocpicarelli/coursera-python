# Conversor de Kelvin para Fahrenheit

K = input("Digite a  temperatura em Kelvin que você deseja converter: ")
K = float(K)
C = K - 273
F = ((9*C)/5)+32
print("A temperatura em Fahrenheit é " + str(F) + '.')
