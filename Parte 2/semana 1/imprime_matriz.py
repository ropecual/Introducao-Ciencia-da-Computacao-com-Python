# minha_matriz = [[1], [2], [3]]
# minha_matriz = [[1, 2, 3], [4, 5, 6]]

#minha_matriz = [[1, 2], [3, 4]]


def imprime_matriz(minha_matriz):
    for i in range(len(minha_matriz)):
        for j in range(len(minha_matriz[i])):
            if j == len(minha_matriz[i]) - 1:
                print(minha_matriz[i][j], end="")
            else:
                print(minha_matriz[i][j], end=" ")
        print()


#imprime_matriz(minha_matriz)
