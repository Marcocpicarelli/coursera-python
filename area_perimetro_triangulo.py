# Programa para calcular a área e perímetro de um triângulo retângulo

import math # Importação do módulo math para usar raiz quadrada

h = float(input("Digite o valor da altura do triângulo: "))
b = float(input("Digite o valor da base do triângulo: "))

area = (b*h)/2
hipotenusa = math.sqrt((b**2) + (h**2))
perimetro = hipotenusa + b + h

print("A área do seu triâgulo é " + str(area) + ".")
print("O perímetro do seu triângulo é " + str(perimetro) + ".")
