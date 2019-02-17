def partida_unica():
    print("Você começa!")
    print()
    pts_computador = 0
    pts_usuario = 0

    escolha = int(input("Digite 1 se você quiser pedra, 2 se você quiser papel ou 3 se você quiser tesoura: "))
    if escolha == 1:
        print("Xi, você escolheu pedra e eu escolhi papel.")
        pts_computador = pts_computador + 1
        print()
        print("Placar: Eu " + str(pts_computador) + " X " + str(pts_usuario) + " Você")
        print()
    elif escolha == 2:
        print("Xi, você escolheu papel e eu escolhi tesoura.")
        pts_computador = pts_computador + 2
        print()
        print("Placar: Eu " + str(pts_computador) + " X " + str(pts_usuario) + " Você")
        print()
    elif escolha == 3:
        print("Xi, você escolheu tesoura e eu escolhi pedra.")
        pts_computador = pts_computador + 3
        print()
        print("Placar: Eu " + str(pts_computador) + " X " + str(pts_usuario) + " Você")
        print()

def melhor_tres():
    contador = 0
    while contador < 3:
        partida_unica()
        contador = contador + 1

def tipo_jogo():
    nome = input("Olá, qual o seu nome? ")
    print("Tudo bem, " + nome + "? Vamos jogar pedra, papel e tesoura! :-)")
    print()
    print("Vamos escolher o tipo de jogo.")
    print()
    print("Digite 1 se você quer jogar uma única partida ou 2 se você quiser jogar uma melhor de três.")
    x = input()
    return x

##### INÍCIO DO PROGRAMA #####

tipo_jogo = tipo_jogo()
acabou = False
while not acabou:
    if tipo_jogo == "1":
        acabou = True
        partida_unica()
    elif tipo_jogo == "2":
        acabou = True
        melhor_tres()
    elif tipo_jogo != "1" and tipo_jogo != "2":
        print("Escolha inválida! Tente novamente.")
        tipo_jogo = input()
print("Fim de jogo!")
