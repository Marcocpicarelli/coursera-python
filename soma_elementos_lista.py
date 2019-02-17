# Escreva a função soma_elementos que recebe como parâmetro uma
# lista com números inteirose devolve um número inteiro
# correspondente à soma dos elementos da lista recebida.

def soma_elementos(lista):
    soma = 0
    contador = 0

    while contador < len(lista):
        soma = soma + lista[contador]
        contador = contador + 1

    return soma

##### INÍCIO DO PROGRAMA #####

lista = []
cont = 0

quantidade = int(input("Quantos números sua lista vai ter? "))

while cont < quantidade:
    n = int(input("Digite o próximo número da lista ou zero para terminar: "))
    cont = cont + 1
    lista.append(n)

print(soma_elementos(lista))

# print("A soma dos elementos da lista é " + str(soma_elementos()))
