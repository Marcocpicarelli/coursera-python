def calcula_soma(a, b):
    soma = a + b
    return soma

def calcula_subtracao(a, b):
    subtracao = a - b
    return subtracao

def calcula_multiplicacao(a, b):
    produto = a * b
    return produto

def calcula_divisao(a, b):
    divisao = a / b
    return divisao

def calcula_divisao_inteira(a, b):
    resultado = a // b
    return resultado

def calcula_resto_divisao(a, b):
    resto = a % b
    return resto

if __name__ == "__main__":
    a = 5
    b = 2
    print(calcula_soma(a, b))
