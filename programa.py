import math

numero = input("digite um numero: ")
i = 0
soma =0
digito = "n"

while i < len(numero):
    if digito != numero[i]:
        digito = numero[i]
    else:
        print("Há digitos subjacentes iguais")
        print("O Digito é", digito)

    soma = soma + int(numero[i])
    i += 1



print("a soma é",soma)