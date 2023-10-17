def busca_sequencial(seq, x):
    '''(list, float) -> bool'''
    for i in range(len(seq)):
        if seq[i] == x:
            return True
    return False


'''
Complexidade Computacional

Analise matematica do desempenho de um algoritmo

Estudo analitico de:
    qntas operacoes um algoritmo requer para que ele seja executado
    quanto tempo ele vai demorar para ser executado
'''

'''
Selecao Direta

A cada passo, busca pelo menor elemento do pedaço ainda nao ordenado da lista e o coloca no inicio da lista

No 1ºpasso, busca o menor elemento de todos e o coloca na posiçao inicial da lista
No 2ºpasso, busca o segundo menor elemento da lista e o coloca na segunda posicao da lista
...
Repete ate terminar a lista
'''


class Ordenador:
    def selecao_direta(self, lista):

        fim = len(lista)
        print(f'FIM {fim}')
        for i in range(fim - 1):
            print(f'Para {i} ate range de {fim - 1}: ')
            # Inicialmente, o menor elemento ja visto eh o i-esimo
            posicao_do_minimo = i
            print(f'posicao minimo: {posicao_do_minimo} == i: {i}')

            for j in range(i + 1, fim):
                print(f'Para {j} ate range de i, {i + 1} ate {fim}: ')
                if lista[j] < lista[posicao_do_minimo]:
                    print(f'Se lista[j]: {lista[j]} eh menor que lista[posicao_do_minimo] {lista[posicao_do_minimo]} ')
                    posicao_do_minimo = j
                    print(f'posicao_do_minimo recebe valor de j: {posicao_do_minimo}')

            # Coloca o menor elemento encontrado no inicio da sub-lista
            # Para isso, troca de lugar os elementos nas posicoes "i" e "posicao_do_minimo"
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
            print(f'lista[i] {lista[i]}')
            print(f'lista: {lista}')
            print(f'lista[posicao_do_minimo] {lista[posicao_do_minimo]}')
            print('--------------------------------------------')


lista = [55, 33, 0, 900, -432, 10, 77, 2, 11]

ordenador = Ordenador()
ordenador.selecao_direta(lista)


# numeros = [55,33,0,900,-432,10,77,123,11]

def busca_sequencial2(seq, x):
    '''(list, float) -> bool'''
    for i in range(len(seq)):
        if seq[i] == x:
            return i
    return -1
