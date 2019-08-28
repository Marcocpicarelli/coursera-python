# Função que calcula a distância entre dois pontos em um plano

import math # Importação do módulo math para usar raiz quadrada

def calcula_dist_pontos(x1, y1, x2, y2):
    distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distancia


