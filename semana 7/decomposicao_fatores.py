numero = int(input("Digite um numero inteiro maior que 1: "))


# De outro jeito
def primo(num):
    fator = 2
    if num == 2 or num == 1:
        return print("Primo")
    while (num % 2) != 0 and fator <= (num / 2):
        fator = fator + 1
    if (num % 2) == 0:
        print("Não é Primo")
    else:
        print("Primo")


fator = 2
multiplicidade = 0
interacao = 1
while numero > 1:
    num_original = numero
    while numero % fator == 0:
        multiplicidade += 1
        numero = numero / fator

    if multiplicidade > 0:
        print("Fator: ", fator, "multiplicidade =", multiplicidade)
    fator += 1
    multiplicidade = 0
    if interacao == 1:
        primo(num_original)
    interacao += 1
