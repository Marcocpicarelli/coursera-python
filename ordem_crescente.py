# Programa que verifica se os números estão em ordem crescente

def verifica_ordem_crescente(x, y, z):
    if x < y < z:
        return "Ordem crescente"
    else:
        return "Tudo cagado"

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

print(verifica_ordem_crescente(a, b, c))
