
lista = [2, 4, 2, 2, 3, 3, 1]


def soma_elementos(lista):
    soma = 0
    for numero in lista:
        soma = numero +soma
    return soma



soma_elementos(lista)