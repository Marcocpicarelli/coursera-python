# Função que verifica se os números estão em ordem decrescente

def ordem_decrescente:

    decrescente = True
    anterior = int(input("Digite o primeiro número da sequência: "))

    valor = 1

    while valor != 0 and decrescente:
        valor = int(input("Digite o próximo número da sequência: "))
        if valor > anterior:
            decrescente = False
        anterior = valor

    if decrescente:
        print("A sequência está em ordem decrescente!")
    else:
        print("A sequência não está em ordem decrescente!")

# Função que verifica se os números estão em ordem crescente

def verifica_ordem_crescente(x, y, z):
    if x < y < z:
        return "Ordem crescente"
    else:
        return "Tudo cagado"

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

print(verifica_ordem_crescente(a, b, c))
