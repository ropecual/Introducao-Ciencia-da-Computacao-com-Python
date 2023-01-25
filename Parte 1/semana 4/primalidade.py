numero = input("Digite um número inteiro: ")

i = 1
count = 0
while i < int(numero):
    if int(numero) % i == 0:
        count += 1
    i += 1
if count > 1:
    print("não primo")
else:
    print("primo")
