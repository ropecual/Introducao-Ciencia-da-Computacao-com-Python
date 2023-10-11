def cria_matriz(linhas, colunas, valor):
    matriz = []
    #  percorre a quantidade de linhas que queremos e,
    for i in range(linhas):
        # para cada numero, adiciona uma linha, se por 4, vai rodar 4  vezes o for e criar 4 linhas
        linha = []
        # percorre a quantidade de colunas que queremos, em cada linha e,
        for j in range(colunas):
            # para cada numero, adiciona o valor na linha, ou seja [1, 2, 3]
            linha.append(valor)
        # ao final, adiciona a linha à matriz
        matriz.append(linha)
    return matriz