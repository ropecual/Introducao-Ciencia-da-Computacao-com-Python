def insertion_sort(lista):
    for i in range(len(lista)):
        if i > 0:
            while lista[i - 1] > lista[i]:
                #print(f'Indice anterior eh {i - 1}, atual eh {i}')
                #print(f'{lista[i - 1]}  maior que {lista[i]}')
                lista[i - 1], lista[i] = lista[i], lista[i - 1]
                #print(f'Invertendo temos {lista[i - 1]}  e {lista[i]}')
                #print('-----------------------------------------------')
                if i > 1:
                    i -= 1

    return lista
