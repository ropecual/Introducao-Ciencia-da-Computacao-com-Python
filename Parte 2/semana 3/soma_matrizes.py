import cria_matriz


def soma_matrizes(a, b):
    num_lin = len(a)
    num_col = len(a[0])

    c = cria_matriz.cria_matriz(num_lin, num_col, 0)

    for lin in range(num_lin):
        for col in range(num_col):
            c[lin][col] = a[lin][col] + b[lin][col]

    return c


if __name__ == '__main__':
    a = [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
    ]

    b = [
        [3, 8, 2],
        [5, 7, 1],
        [3, 6, 7],
    ]


    print(soma_matrizes(a,b))