import math

a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))


def delta(a, b, c):
    return (b ** 2) - (4 * a * c)


def x1(a, b, delta):
    return (-b + math.sqrt(delta)) / (2 * a)


def x2(a, b, delta):
    return (-b - math.sqrt(delta)) / (2 * a)


delta = delta(a, b, c)
xum = x1(a, b, delta)
xdois = x2(a, b, delta)

if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    print("a raiz desta equação é", x1)
else:
    print("as raízes da equação são", xdois, "e", xum)
