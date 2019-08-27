# Cálculos de perímetro e área de um quadrado

def calcula_area_quadrado(lado):
    area = lado**2
    return area

def calcula_perimetro_quadrado(lado):
    perimetro = 4 * lado
    return perimetro

n = int(input("Digite o valor correspondente ao lado de um quadrado: "))

print(calcula_area_quadrado(n))

print(calcula_perimetro_quadrado(n))
