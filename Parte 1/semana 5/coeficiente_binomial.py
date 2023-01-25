n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k "))


def fatorial(numero):
    fat = 1
    while numero > 1:
        fat = fat * numero
        numero = numero - 1
    return fat


def num_binomial(n, k):
    if n < k:
        print("Não é possível executar o calculo")
        return 0
    else:
        return fatorial(n) / (fatorial(k) * fatorial(n - k))


print(num_binomial(n, k))
