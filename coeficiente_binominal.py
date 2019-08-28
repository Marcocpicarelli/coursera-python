import fatorial

def coef_binominal(n, k): # Definição de função que calcula o coeficiente binominal
    
    coef = fatorial.fatorial(n) / (fatorial.fatorial(k) * (fatorial.fatorial(n-k))) # Função fatorial chamada três vezes
    coef = int(coef)

    return coef




