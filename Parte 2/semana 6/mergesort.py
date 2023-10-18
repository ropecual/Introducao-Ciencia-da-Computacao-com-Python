# Ordenacao por intercalacao
import random
import time


# Divida a lista na metade, recursivamente, ate que cada sublista contenha apenas 1 elemento, portanto, ja ordenada

# Repetidamente, intercale as sublistas para produzir NOVAS listas ordenadas


def merge_sort(lista):
    print(f'Lista atual {lista}')
    if len(lista) <= 1:   # Base da recursao
        return lista

    meio = len(lista) // 2

    lado_esquerdo = merge_sort(lista[:meio])
    lado_direito = merge_sort(lista[meio:])

    return merge(lado_esquerdo, lado_direito)


def merge(lado_esquerdo, lado_direito):
    print(f'Entrou no Merge')
    if not lado_esquerdo:
        print(f'Sem lado esquerdo, retornando {lado_direito}')
        return lado_direito

    if not lado_direito:
        print(f'Sem lado direito, retornando {lado_esquerdo}')
        return lado_esquerdo

    if lado_esquerdo[0] < lado_direito[0]:
        print('Lado esquerdo menor')
        print(f'{[lado_esquerdo[0]]} + merge({lado_esquerdo[1:]}, {lado_direito})')
        print('----------------')
        return [lado_esquerdo[0]] + merge(lado_esquerdo[1:], lado_direito)

    print('Lado direito maior')
    print(f'{[lado_direito[0]]} + merge({lado_esquerdo}, {lado_direito[1:]}')
    print('----------------')
    return [lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])



def lista_grande(n):
    inicio = time.time()
    lista = [random.randint(-100, 100) for x in range(n)]
    fim = time.time()
    print(f'Tempo para geração da lista: {fim - inicio:.2} segundos')
    return lista


lista = lista_grande(10)


print(merge_sort(lista))