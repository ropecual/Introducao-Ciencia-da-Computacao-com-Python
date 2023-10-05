def cria_matriz(num_linhas, num_colunas):
    matriz = []  # Lista vazia

    for i in range(num_linhas):
        linha = []  # Cria a linha i
        for j in range(num_colunas):  # Percorre a linha adicionando as colunas com o valor
            linha.append(int(input(f"Insira um valor para a linha {i} e coluna {j}: ")))

        matriz.append(linha)  # Adiciona a linha à matriz

    return matriz


# print(cria_matriz(2,3))

def cria_matriz(num_linhas, num_colunas):
    matriz = []  # Lista vazia

    for i in range(num_linhas):
        linha = []  # Cria a linha i
        for j in range(num_colunas):  # Percorre a linha adicionando as colunas com o valor
            linha.append(0)
        matriz.append(linha)

    for i in range(num_colunas):
        for j in range(num_linhas):
            matriz[j][i] = (int(input(f"Insira um valor para a linha {i} e coluna {j}: ")))

    return matriz


print(cria_matriz(2, 3))


def tarefa(mat):
    dim = len(mat)
    for i in range(dim):
        print(mat[i][dim - 1 - i], end=" ")


mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# tarefa(mat)
