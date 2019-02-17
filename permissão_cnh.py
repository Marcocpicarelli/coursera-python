# Verificar se motorista tem permissão para dirigir

idade = int(input("Qual a idade do motorista? "))
if idade < 18:
    restante = 18 - idade
    print("Opa! Esse motorista ainda não tem permissão para dirigir.")
    print("Aguarde " + str(restante) + " ano(s) para tirar a CNH.")
else:
    print("Esse motorista tem 18 anos ou mais e está autorizado a dirigir.")
