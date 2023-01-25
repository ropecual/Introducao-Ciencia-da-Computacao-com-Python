import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)


def compara_assinatura(as_a, as_b):
    ''' Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    i = 0
    resultado = 0
    if len(as_a) == len(as_b):
        while i < len(as_a):
            resultado = resultado + abs(as_a[i] - as_b[i])
            i += 1
        return resultado / 6


def calcula_assinatura(texto):
    assinatura = []
    count_sentencas = 0
    count_frases = 0
    count_caracteres = 0
    lista_palavras = []
    caracteres_frases = 0
    caracteres_sentencas = 0

    total_palavras = len(separa_palavras(texto))

    for sentenca in separa_sentencas(texto):
        caracteres_sentencas = caracteres_sentencas + len(sentenca)
        count_sentencas += 1

        for frase in separa_frases(sentenca):
            caracteres_frases = caracteres_frases + len(frase)
            count_frases += 1

            for palavra in separa_palavras(frase):
                lista_palavras.append(palavra)

                for caractere in palavra:
                    count_caracteres += 1

    wal = count_caracteres / total_palavras
    assinatura.append(wal)
    ttr = n_palavras_diferentes(lista_palavras) / total_palavras
    assinatura.append(ttr)
    hlr = n_palavras_unicas(lista_palavras) / total_palavras
    assinatura.append(hlr)
    sal = caracteres_sentencas / count_sentencas
    assinatura.append(sal)
    sac = count_frases / count_sentencas
    assinatura.append(sac)
    pal = caracteres_frases / count_frases
    assinatura.append(pal)
    return assinatura


def avalia_textos(textos, ass_cp):
    ''' Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    valores = []
    for texto in textos:
        valores.append(compara_assinatura(calcula_assinatura(texto), ass_cp))
    return menor_elemento(valores)


def menor_elemento(lista):
    aux = lista[0]
    posicao = 0
    i = 1
    while i <= len(lista):
        if aux >= lista[i - 1]:
            aux = lista[i - 1]
            posicao = i
        i += 1
    return posicao
