import math

x1 = float(input("Valor de x1: "))
y1 = float(input("Valor de y1: "))
x2 = float(input("Valor de x2: "))
y2 = float(input("Valor de y2: "))

distancia = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

if distancia >= 10:
    print("longe")
    print(distancia)
else:
    print("perto")
    print(distancia)
