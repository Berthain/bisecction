import math
print("BISECTION")

# as raízes já devem ter sido encontradas
a = 0.78
b = 0.80
x = 0.0
# precisão solicitada
p = 0.001


def iteracoes(a, b, p):
    iteracoes = int((math.log(b-a) - math.log(p))/math.log(2))
    iteracoes += 1
    return iteracoes


def media(a, b):
    x = (a+b)/2
    return float(x)


def comparaxb_funcs(a, b):
    fa = funcX(a)
    fb = funcX(b)
    # Verificar sinal dos extremos
    la = fa * fb < 0
    return la


def funcX(x):
    fx = 0.0
    # fx = 4 * math.cos(x) - math.exp(x)
    # fx = 3*math.pow(x, 5) + 6*math.pow(x, 2) - x + 1
    # fx = math.log(x) - 3*math.pow(x, 2) + 5
    fx = -4*math.pow(x, 7) - 3*math.pow(x, 3) - math.pow(x, 2) + 3
    # fx = math.log(x) - 2*math.sin(x)
    return round(fx, 4)


def erro(a, b):
    e = (b-a)/2
    if e < 0:
        e *= (-1)
    return e


# print("nova b", b)
final = iteracoes(a, b, p)
x = media(a, b)

print("I ", "  a   ", "   b  ", "  x   ", " f(a) ", " f(b) ", " f(x) ")

for count in range(1, final+1):
    print(count, " ", 
          round(a, 4),  "  ", 
          round(b, 4),  "  ", 
          round(x, 4),  "  ", 
          funcX(a), "  ", 
          funcX(b), "  ", 
          funcX(x))
    if comparaxb_funcs(a, x):
        b = x
    else:
        a = x
    x = media(a, b)
