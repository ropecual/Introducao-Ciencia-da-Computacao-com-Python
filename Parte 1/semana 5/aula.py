def fatorial(numero):
    fat = 1
    while numero > 1:
        fat = fat * numero
        numero = numero - 1
    return fat


print(fatorial(2))