
def busca(lista, x):
    primeiro = 0
    ultimo = len(lista) - 1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        print(meio)
        if lista[meio] == x:
            return meio
        else:
            if x < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1

    return False







#print(busca(['a', 'e', 'i'], 'e'))

# deve devolver => 1

#print(busca([1, 2, 3, 4, 5], 6))

# deve devolver => False

#print(busca([1, 2, 3, 4, 5, 6], 4))

# deve devolver => 3