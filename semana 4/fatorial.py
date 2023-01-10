numero = int(input("Digite o valor de n: "))

i = 1
fatorial = numero
if numero == 0:
    fatorial = 1
else:
    while i < numero:
        fatorial = fatorial * (numero - i)
        i += 1

print(fatorial)
