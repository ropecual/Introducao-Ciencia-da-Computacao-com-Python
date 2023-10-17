"""
Como em um tubo de ensaio vertical, onde os elementos mais leves sobem à superficie e os mais pesados afundam

Percorre a lista múltiplas vezes; a cada passagem, compara todos os elementos adjacentes e troa de lugar os que
estiverem fora de ordem

A cada passagem, o elemento mais pesado se deposita no fundo do tubo de ensaio; i.e., o maior elemento da lista vai para
o final dela

5 1 1 1
1 5 3 2
7 3 2 3
3 2 5 5
2 7 7 7
"""
import random
import time


def lista_grande(n):
    inicio = time.time()
    lista = [random.randint(-10000, 10000) for x in range(n)]
    fim = time.time()
    print(f'Tempo para geração da lista: {fim - inicio:.2} segundos')
    return lista


class Ordenador:
    def selecao_direta(self, lista):
        fim = len(lista)
        for i in range(fim - 1):
            posicao_do_minimo = i
            for j in range(i + 1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
        return lista

    def bolha(self, lista):
        fim = len(lista)
        for i in range(fim - 1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista

    # Bolha melhorada, verifica se foi feita a troca, se n fizer, a lista já está ordenada
    def bolha_melhorada(self, lista):
        fim = len(lista)
        for i in range(fim - 1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    trocou = True
            if not trocou:
                return lista

        return lista

    def insercao(self, lista):
        for i in range(len(lista)):
            if i > 0:
                while lista[i - 1] > lista[i]:
                    lista[i - 1], lista[i] = lista[i], lista[i - 1]
                    if i > 1:
                        i -= 1
        return lista

#lista_gigante = lista_grande(50)
lista_gigante = [1,2,3,4,5]
ordenador = Ordenador()
print('----------------------------------------------------------------------')
inicio = time.time()
print((ordenador.bolha(lista_gigante)))
fim = time.time()
print(f'Tempo para ordenação bolha da lista: {fim - inicio:.2} segundos')
print('----------------------------------------------------------------------')
inicio = time.time()
print((ordenador.bolha_melhorada(lista_gigante)))
fim = time.time()
print(f'Tempo para ordenação bolha melhorada da lista: {fim - inicio:.2} segundos')
print('----------------------------------------------------------------------')
inicio = time.time()
print((ordenador.selecao_direta(lista_gigante)))
fim = time.time()
print(f'Tempo para ordenação direta da lista: {fim - inicio:.2} segundos')
print('----------------------------------------------------------------------')

inicio = time.time()
print((ordenador.insercao(lista_gigante)))
fim = time.time()
print(f'Tempo para insercao da lista: {fim - inicio:.2} segundos')
