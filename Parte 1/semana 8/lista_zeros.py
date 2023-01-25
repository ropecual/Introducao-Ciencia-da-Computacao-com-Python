i = 0
n = "n"
lista = []
while n != 0:
    n = int(input("Digite os números que deseja, '0' para sair: "))
    lista.append(n)

for i in range(len(lista)):
    print(lista[len(lista)-i-1])

