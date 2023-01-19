import math

def soma_hipotenusas(n):
    i = 1
    soma = 0
    while i <= n:
        if é_hipotenusa(i):
            soma = soma + i
        i += 1
    return soma


def é_hipotenusa(num):
    i = 1
    j = 1
    while i < num:
        while j < num:
            resultado = math.sqrt((i ** 2) + (j ** 2))
            if resultado == num:
                return True
            j += 1
        j = 1
        i += 1



