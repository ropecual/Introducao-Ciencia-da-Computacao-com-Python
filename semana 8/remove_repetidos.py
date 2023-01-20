lista = [2, 4, 2, 2, 3, 3, 1]


def remove_repetidos(lista):
    ordenada = []
    for numero in lista:
        if numero not in ordenada:
            ordenada.append(numero)

    return sorted(ordenada)


remove_repetidos(lista)
