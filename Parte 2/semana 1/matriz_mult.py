m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]

m1 = [[1], [2], [3]]
m2 = [[1, 2, 3]]

def dimensoes(minha_matriz):
    cont_i = 0
    for i in range(len(minha_matriz)):
        cont_i = cont_i + 1
        cont_j = 0
        for j in range(len(minha_matriz[i])):
            cont_j = cont_j + 1

    return cont_i, cont_j


def sao_multiplicaveis(m1,m2):
    m1_i, m1_j = dimensoes(m1)
    m2_i, m2_j = dimensoes(m2)

    if m1_j == m2_i:
        return True
    else:
        return False


print(sao_multiplicaveis(m1,m2))