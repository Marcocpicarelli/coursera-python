# Programa que calcula a distância entre dois pontos em um plano

import math # Imporatação do módulo math para usar raiz quadrada

def calcula_dist_pontos(x1, y1, x2, y2):
    distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distancia

a = int(input("Digite o valor do eixo x do primeiro ponto: "))
b = int(input("Digite o valor do eixo y do primeiro ponto: "))
c = int(input("Digite o valor do eixo x do segundo ponto: "))
d = int(input("Digite o valor do eixo y do segundo ponto: "))

print(calcula_dist_pontos(a, b, c, d))


