i = 0
n = "n"
lista = []
while n != 0:
    n = int(input("Digite um número: "))
    if n != 0:
        lista.append(n)

for i in range(len(lista)):
    print(lista[len(lista) - i - 1])
