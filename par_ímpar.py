# Programa que verifica se um número é par ou ímpar

def verifica_par_impar(n):
    if n % 2 == 0: # Verifica se o resto da divisão dá zero
        return "Par"
    else:
        return "Ímpar"

x = int(input("Digite um número: "))

print(verifica_par_impar(x))

