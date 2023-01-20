lista = [2, 4, 2, 2, 3, 3, 1]


def maior_elemento(lista):
    aux = -500000000000000
    for numero in lista:
        if aux <= numero:
            aux = numero
    return aux


maior_elemento(lista)
