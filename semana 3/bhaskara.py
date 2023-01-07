import math

a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))

delta = b ** 2 - 4 * a * c
x1 = 0
x2 = 0

if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    print("a raiz desta equação é",x1)
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("as raízes da equação são",x2,"e",x1)