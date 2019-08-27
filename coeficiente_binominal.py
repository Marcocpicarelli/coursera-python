def fatorial(x): # Definição da função que calcula o fatorial de um número
    fatorial = 1
    cont = 1

    if x == 0:
        fatorial = 1
    else:
        while cont <= x:
            fatorial = fatorial * cont
            cont = cont + 1

    return fatorial

def coef_binominal(n, k): # Definição de função que calcula o coeficiente binominal
    
    coef = fatorial(n) / (fatorial(k) * (fatorial(n-k))) # Função fatorial chamada três vezes
    coef = int(coef)

    return coef

############ INÍCIO DO PROGRAMA #############

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print(coef_binominal(a, b)) # Chamada da função de coeficiente binominal




