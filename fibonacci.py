# Funções que mostram a sequência de Fibonacci
# até o valor n determinado pelo usuário

def calcula_fib(n): # Essa imprime cada número individualmente
    a, b = 0, 1
    while b < n:
        print(b, end = "")
        a, b = b, a + b
    print()

def calcula_fib2(n): # Essa retorna em lista
    resultado = []
    a, b = 0, 1
    while b < n:
        resultado.append(b)
        a, b = b, a + b
    return resultado
