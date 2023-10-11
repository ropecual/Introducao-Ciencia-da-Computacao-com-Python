def menor_nome(lista_string):
    menor = lista_string[0].strip()
    for string in lista_string:
        if len(string.strip()) < len(menor.strip()):
            menor = string.strip()
    return menor.capitalize()


