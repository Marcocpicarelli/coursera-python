# Escrever uma função que recebe uma lista de strings
# contendo nomes de pessoas como parâmetros e devolve
# o nome mais curto. A função deve ignorar espaços antes
# e depois do nome e deve devolver o nome com
# "capitalização", i.e., apenas com a primeira letra em
# maiúscula.

def nome_mais_curto(lista):
    nome_anterior = ""
    for nome in lista:
        nome = nome.strip()
        if len(nome) < len(nome_anterior) or nome_anterior == "":
            nome_selecionado = nome
            nome_anterior = nome
    nome_selecionado = nome_selecionado.capitalize()            
    return nome_selecionado

def testa_mais_curto():
    if nome_mais_curto(["   luciana ", "        PaUlO     ", "  AnA    ", "JEFFERSON      "]) == "Ana":
        print("A função está funcionando.")
    else:
        print("A função não está funcionando.")
