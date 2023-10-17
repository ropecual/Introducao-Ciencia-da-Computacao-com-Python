# Considere o elemento M do meio da lista
# Se X == M => Encontrou
# Se X < m => procurar apenas na primeira metade
# Repetir ate encontrar
# Se X > M procurar na segunda metade
# Repetir ate encontrar


# Dado uma linsta de n elementos
# No pior caso, teremos que efetuar - Log2 n comparacoes

import time


def lista_grande_sequencial(n):
    lista = [x for x in range(n)]
    return lista


class Buscador:
    def busca_sequencial(self, lista, x):
        for i in range(len(lista)):
            if lista[i] == x:
                return i

        return -1

    def busca_binaria(self, lista, x):
        primeiro = 0
        ultimo = len(lista) - 1

        while primeiro <= ultimo:
            meio = (primeiro + ultimo) // 2
            if lista[meio] == x:
                return meio
            else:
                if x < lista[meio]:
                    ultimo = meio - 1
                else:
                    primeiro = meio + 1

        return -1


lista = lista_grande_sequencial(200_000_000)
buscador = Buscador()
print('----------------------------------------------------------------------')
inicio = time.time()
buscador.busca_sequencial(lista, 199_999_999)
fim = time.time()
print(f'Tempo para busca sequencial da lista: {fim - inicio} segundos')
print('----------------------------------------------------------------------')
inicio = time.time()
buscador.busca_binaria(lista, 199_999_999)
fim = time.time()
print(f'Tempo para busca binaria da lista: {fim - inicio} segundos')