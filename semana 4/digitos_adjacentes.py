numero = input("Digite o valor de n: ")


i = 0
valor = "n"
count = 0

while i < len(numero):
    if valor != numero[i]:
        valor = numero[i]
    else:
        count += 1
    i += 1

if count > 0:
    print("sim")
else:
    print("não")
