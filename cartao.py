meucartao = int(input("Digite o número do seu cartão de crédito: "))

cartaolido = 1
encontreimeucartao = False

while cartaolido != 0 and not encontreimeucartao:
    cartaolido = int(input("Digite o número do próximo cartão de crédito: "))
    if cartaolido == meucartao:
        encontreimeucartao == True

if encontreimeucartao:
    print("Eba! Meu cartão está lá!")
else:
    print("Xi, meu cartão não está lá...")
