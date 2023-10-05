"""
Lista armazenam uma coleção linear de valores. Matrizes por outro lado, são listas de listas,  Linhas x Colunas.
É uma estrutura de dados bidimencional com linhas e colunas

Exemplo:

A =
1 2 3
4 5 6
7 8 9

para acessar cada elemento da matriz utilizamos o seguinte modelo MATRIZ[X][X], onde o primeiro X representa a LINHA e
o segundo a COLUNA

logo, A[0][0] = 1 ou A[2][1] = 8

"""

A = [
    [1, 2, 3],
    [4, 5, 6, 'X'],
    [7, 8, 9],
    [10, 11, 12],
]
# print(A)

'''
Cria e retorna uma matriz com num_linhas e num_colunas em que cada elemento é igual ao valor dado
'''


def cria_matriz(num_linhas, num_colunas, valor):
    matriz = []  # Lista vazia

    for i in range(num_linhas):
        linha = []  # Cria a linha i
        for j in range(num_colunas):  # Percorre a linha adicionando as colunas com o valor
            linha.append(valor)

        matriz.append(linha)  # Adiciona a linha à matriz

    return matriz


def imprime_matriz_1(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="")
        print()


def imprime_matriz_2(matriz):
    for i in range(len(matriz)):
        print(matriz[i])


imprime_matriz_1(A)
print()
imprime_matriz_2(A)


def cria_matriz_com_input():
    num_linhas = int(input("Insira a quantidade de linhas: "))
    num_colunas = int(input("Insira a quantidade de Colunas: "))
    matriz = []  # Lista vazia

    for i in range(num_linhas):
        linha = []  # Cria a linha i
        for j in range(num_colunas):  # Percorre a linha adicionando as colunas com o valor
            linha.append(int(input(f"Insira um valor para a linha {i} e coluna {j}: ")))

        matriz.append(linha)  # Adiciona a linha à matriz

    return matriz


#imprimi_matriz_2(cria_matriz_com_input())
