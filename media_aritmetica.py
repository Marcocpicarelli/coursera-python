# Cálculo de média aritmética de quatro notas

def calcula_media(a, b, c, d):
    media = (a + b + c + d) / 4
    return media

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))

print(calcula_media(nota1, nota2, nota3, nota4))
