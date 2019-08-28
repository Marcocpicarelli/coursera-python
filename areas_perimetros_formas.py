import math # Importação do módulo math para usar raiz quadrada

# Função que calcula a área de uma circunferência

def calcula_area_circunf(r):
    pi = 3.14
    pi = float(pi)
    area = pi*(r**2)
    return area

# Função que calcula o perímetro de uma circunferência

def calcula_perimetro_circunf(r):
    pi = 3.14
    pi = float(pi)
    perimetro = 2*pi*r
    return perimetro

# Função que calcula a área de um triângulo

def calcula_area_triangulo(b, h):
    area = (b*h)/2
    return area

# Função que calcula o perímetro de um triângulo

def calcula_perimetro_triangulo(b, h):
    hipotenusa = math.sqrt((b**2) + (h**2))
    perimetro = hipotenusa + b + h
    return perimetro

# Função que calcula a área de um quadrado

def calcula_area_quadrado(lado):
    area = lado**2
    return area

# Função que calcula o perímetro de um quadrado

def calcula_perimetro_quadrado(lado):
    perimetro = 4 * lado
    return perimetro
