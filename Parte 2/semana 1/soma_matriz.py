m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]


def dimensoes(minha_matriz):
    cont_i = 0
    for i in range(len(minha_matriz)):
        cont_i = cont_i + 1
        cont_j = 0
        for j in range(len(minha_matriz[i])):
            cont_j = cont_j + 1

    return cont_i, cont_j


def soma_matrizes(m1, m2):
    m1_i, m1_j = dimensoes(m1)
    m2_i, m2_j = dimensoes(m2)

    if m1_i == m2_i and m1_j == m2_j:
        soma_matriz = []
        for i in range(m1_i):
            linha = []
            for j in range(m1_j):
                linha.append(m1[i][j] + m2[i][j])
            soma_matriz.append(linha)
        return soma_matriz
    else:
        return False


print(soma_matrizes(m1, m2))
