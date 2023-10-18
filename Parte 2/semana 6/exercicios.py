def x(n):
    if n == 0:
        print(n)
    else:

        x(n - 1)
        print(n)


def doisx(n, m):
    if n == m or m == 0:
        return 1
    else:
        return doisx(n - 1, m) + doisx(n - 1, m + 1)


def tresx(n):
    if n >= 0 or n <= 2:
        return n
    else:
        return tresx(n - 1) + tresx(n - 2) + tresx(n - 3)

#print(tresx(6))



def quatrox(n):
    print(n)
    if n >= 0 and n <= 2:
        return n
    else:

        return quatrox(n - 1) + quatrox(n - 2) + quatrox(n - 3)

print(quatrox(6))









def busca_binaria_recursiva(lista, elemento, min=0, max=None):

    if max == None:
        max = len(lista) - 1

    if max < min:
        return False
    else:
        meio = min + (max - min) // 2
    print(f'recursiva: {lista[meio]}')
    if lista[meio] > elemento:
        return busca_binaria_recursiva(lista, elemento, min, meio - 1)
    elif lista[meio] < elemento:
        return busca_binaria_recursiva(lista, elemento, meio + 1, max)
    else:
        return meio



a = [-10, -2, 0, 5, 66, 77, 99, 102, 239, 567, 875, 934]

busca_binaria_recursiva(a, 99)