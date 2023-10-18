# a = [10, 20, 30, 40, 50, 60]


def soma_lista(lista):
    # print(f'Inteiracao da lista: {lista}')
    if len(lista) <= 1:
        return lista[0]

    lista[0] += soma_lista(lista[1:])
    return lista[0]

# lista = [2,1,1,5]
# print(soma_lista(a))
