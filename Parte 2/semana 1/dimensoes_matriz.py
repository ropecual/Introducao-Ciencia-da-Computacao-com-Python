minha_matriz = [
    [1],
    [2],
    [3],
]


def dimensoes(minha_matriz):
    cont_i = 0
    for i in range(len(minha_matriz)):
        cont_i = cont_i + 1
        cont_j = 0
        for j in range(len(minha_matriz[i])):
            cont_j = cont_j + 1

    print(f'{cont_i}x{cont_j}')


dimensoes(minha_matriz)
