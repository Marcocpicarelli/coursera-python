# Programa para calcular a área e perímetro de um triângulo retângulo

import math # Importação do módulo math para usar raiz quadrada

def calcula_area_triangulo(b, h):
    area = (b*h)/2
    return area

def calcula_perimetro_triangulo(b, h):
    hipotenusa = math.sqrt((b**2) + (h**2))
    perimetro = hipotenusa + b + h
    return perimetro

x = float(input("Digite o valor da altura do triângulo: "))
y = float(input("Digite o valor da base do triângulo: "))

print(calcula_area_triangulo(x, y))
print(calcula_perimetro_triangulo(x, y))
