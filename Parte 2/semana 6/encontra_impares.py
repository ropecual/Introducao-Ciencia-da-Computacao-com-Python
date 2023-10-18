def encontra_impares(lista):
    # quando a lista for vazia, ou seja, passou por toda a recursao, devolvemos ela mesma
    if len(lista) <= 0:
        return lista

    # Supondo a lista 1,2,3
    # Ela n sendo vazia, possuindo tamanho 3 temos o primeiro elemento (lista[0]) sendo o 1, esse sendo impar
    if lista[0] % 2 != 0:
        # Criamos uma nova lista e adicionamos o primeiro elemento, que no caso eh o 1
        nova_lista = [lista[0]]
        # adicionamos a nova lista a recursao da mesma, com o proximo elemento da lista em diante, ou seja, a lista tera
        # tamanho 2, sendo agora, seu primeiro elemento o 2, indo para a condicao de par
        nova_lista.extend(encontra_impares(lista[1:]))
        return nova_lista
    else:
        # O elemento sendo par, ativamos a recursao novamente, enviando a lista com o proximo elemento em diante, a
        # lista tera 1 elemento, esse sendo o 3, voltamos a condicao de impar
        return encontra_impares(lista[1:])


#print(encontra_impares([1,2,3]))
