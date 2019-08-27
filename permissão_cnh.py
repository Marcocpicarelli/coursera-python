# Verificar se motorista tem permissão para dirigir

def permissao_dirigir(idade):
    if idade < 18:
        return "Não"
    else:
        return "Sim"

n = int(input("Qual a idade do motorista? "))

print(permissao_dirigir(n))
