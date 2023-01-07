numero = input("Digite um número inteiro: ")


i = 0
soma = 0
while i < len(numero):
    soma = soma + int(numero[i])
    i += 1

print(soma)
