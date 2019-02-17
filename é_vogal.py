a = "a"
A = "A"
b = "b"
B = "B"
c = "c"
C = "C"
d = "d"
D = "D"
e = "e"
E = "E"
f = "f"
F = "F"
g = "g"
G = "G"
h = "h"
H = "H"
i = "i"
I = "I"
j = "j"
J = "J"
k = "k"
K = "K"
l = "l"
L = "L"
m = "m"
M = "M"
n = "n"
N = "N"
o = "o"
O = "O"
p = "p"
P = "P"
q = "q"
Q = "Q"
r = "r"
R = "R"
s = "s"
S = "S"
t = "t"
T = "T"
u = "u"
U = "U"
v = "v"
V = "V"
w = "w"
W = "W"
x = "x"
X = "X"
y = "y"
Y = "Y"
z = "z"
Z = "Z"

##### FUNÇÃO QUE CHECA SE A LETRA É VOGAL #####

def vogal(teste):
        
    if teste == a:
        é_vogal = True
    elif teste == A:
        é_vogal = True
    elif teste == e:
        é_vogal = True
    elif teste == E:
        é_vogal = True
    elif teste == i:
        é_vogal = True
    elif teste == I:
        é_vogal = True
    elif teste == o:
        é_vogal = True
    elif teste == O:
        é_vogal = True
    elif teste == u:
        é_vogal = True
    elif teste == U:
        é_vogal = True
    elif teste == b:
        é_vogal = False
    elif teste == B:
        é_vogal = False
    elif teste == c:
        é_vogal = False
    elif teste == C:
        é_vogal = False
    elif teste == d:
        é_vogal = False
    elif teste == D:
        é_vogal = False
    elif teste == f:
        é_vogal = False
    elif teste == F:
        é_vogal = False
    elif teste == g:
        é_vogal = False
    elif teste == G:
        é_vogal = False
    elif teste == h:
        é_vogal = False
    elif teste == H:
        é_vogal = False
    elif teste == j:
        é_vogal = False
    elif teste == J:
        é_vogal = False
    elif teste == k:
        é_vogal = False
    elif teste == K:
        é_vogal = False
    elif teste == l:
        é_vogal = False
    elif teste == L:
        é_vogal = False
    elif teste == m:
        é_vogal = False
    elif teste == M:
        é_vogal = False
    elif teste == n:
        é_vogal = False
    elif teste == N:
        é_vogal = False
    elif teste == p:
        é_vogal = False
    elif teste == P:
        é_vogal = False
    elif teste == q:
        é_vogal = False
    elif teste == Q:
        é_vogal = False
    elif teste == r:
        é_vogal = False
    elif teste == R:
        é_vogal = False
    elif teste == s:
        é_vogal = False
    elif teste == S:
        é_vogal = False
    elif teste == t:
        é_vogal = False
    elif teste == T:
        é_vogal = False
    elif teste == v:
        é_vogal = False
    elif teste == V:
        é_vogal = False
    elif teste == w:
        é_vogal = False
    elif teste == W:
        é_vogal = False
    elif teste == x:
        é_vogal = False
    elif teste == X:
        é_vogal = False
    elif teste == y:
        é_vogal = False
    elif teste == Y:
        é_vogal = False
    elif teste == z:
        é_vogal = False
    elif teste == Z:
        é_vogal = False
        
    return é_vogal

##### INÍCIO DO PROGRAMA #####

letra = input("Digite uma letra do alfabeto: ")

print(vogal(letra))
