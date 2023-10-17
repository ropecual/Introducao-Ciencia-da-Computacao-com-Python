def ordenada(lista):
    lista_original = lista.copy()
    fim = len(lista)
    for i in range(fim - 1):
        posicao_do_minimo = i
        for j in range(i + 1, fim):
            if lista[j] < lista[posicao_do_minimo]:
                posicao_do_minimo = j
        lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
    for i in range(len(lista_original)):
        if lista[i] != lista_original[i]:
            return False
    return True



