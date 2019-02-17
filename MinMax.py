def MinMax(temperatura):
    print("A menor temperatura do mês foi: ", + minina(temperaturas), + "°C.")
    print("A maior temperatura do mês foi: ", + maxima(temperaturas), + "°C.")

def minima(temps):
    min = temps[0]
    cont = 1

    while cont < len(temps):
        if temps[cont] < min:
            min = temps[cont]
        cont = cont + 1
    return min

def testa_minima():
    print("Iniciando os testes.")
    teste_pontual = ([0], 0)
    teste_pontual = ([0, 0, 0, 0, 0, 0], 0)
    teste_pontual = ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
    teste_pontual = ([-15, -12, 0, 20, 30], -15)
    print("Finalizando os testes.")

def teste_pontual(temp, valor_esperado):
    valor_calculado = minima(temp)
    if valor_calculado != valor_esperado:
        print("Valor errado para o array " + temp + "."
        print("O valor esperado era: " + str(valor_esperado) + ". Valor calculado: " + str(valor_calculado) + ".")

def maxima(temps):
    max = temps[0]
    cont = 1

    while cont < len[temps]:
        if temps[cont] > max:
            max = temps[cont]
        cont = cont + 1
    return max
