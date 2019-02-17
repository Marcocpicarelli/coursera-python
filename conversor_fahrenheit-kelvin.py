# Conversor de Fahrenheit para Kelvin

F = input("Digite a  temperatura em Fahrenheit que você deseja converter: ")
F = float(F)
C = ((F - 32)*5)/9
K = C + 273
print("A temperatura em Kelvin é " + str(K) + '.')
