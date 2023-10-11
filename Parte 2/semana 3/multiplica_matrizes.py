def multiplica_matrizes(a, b):
    num_linhas_a, num_colunas_a = len(a), len(a[0])
    num_linhas_b, num_colunas_b = len(b), len(b[0])
    if num_linhas_a == num_colunas_b:
        c = []
        for linha in range(num_linhas_a):
            # adiciona uma linha nova na matriz resultante
            c.append([])
            for coluna in range(num_colunas_b):
                # adiciona uma coluna na linha da matriz resultante, com valor zero, para inicializa-la
                c[linha].append(0)
                for k in range(num_colunas_a):
                    # percorre o numero de colunas de A;
                    # para a posição de c[linha][coluna] efetua a vetorização, pegando a linha
                    c[linha][coluna] += a[linha][k] * b[k][coluna]

        return c


if __name__ == '__main__':
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [4, 5, 6],
        [4, 5, 6],

    ]

    b = [
        [3, 8, 3, 8],
        [5, 7, 3, 8],
        [5, 7, 3, 8]

    ]

    print(multiplica_matrizes(a, b))
