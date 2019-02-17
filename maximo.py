##### FUNÇÃO QUE RETORNA O MAIOR NÚMERO DIGITADO PELO USUÁRIO #####

def maximo (x, y, z):
    if x > y and  x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > x and z > y:
        return z
    elif x == y == z:
        return x

##### INÍCIO DO PROGRAMA #####

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

print(maximo(a, b, c))
