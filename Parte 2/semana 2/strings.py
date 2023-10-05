palavra = 'aBc d ' * 3

print(palavra)
print(palavra[0])
print(palavra[-1])

# Funções e metodos do string

print(palavra.lower())
print(palavra.upper())
print(palavra.capitalize())
print('OI')
print(palavra.strip())  # Remove espaços em branco ao final e no inicio
print(palavra.count("a"))  # Conta a quantidade da letra buscada
print(palavra.replace("aBc", "teste"))  # troca um termo por outro

frase = 'Grande frase e queremos achar um termo ou caracter'
print(frase.find("t"))
print(frase.find("fr"))
print(frase.find("lalala"))  # -1 significa que não está presente
print(len(frase))

print(frase[:4])
print(frase[:1])
print(frase[2:4])

lista_string = ['chimito', 'ariel', 'anakin', 'lili ', 'supino', 'galadriel']


def mais_curto(lista_string):
    menor = lista_string[0]
    for string in lista_string:

        if len(string.strip()) < len(menor.strip()):
            menor = string.strip()

    print(menor.capitalize())


mais_curto(lista_string)


# Comparação de strings

x = 'teoria'
y = 'pratica'
z = 'teoria'

print(x == y)
print(x != y)
print(x == z)
print(x is z) # Sendo Strings IMUTAVEIS, ou seja, já alocadas na memoria, tanto x, qnto z, apontam para o mesmo local


print(x > y) # Devido a ordem lexografica, Teoria vem depois de pratica.
# Usando o ord é possivel saber a ordenacao no padrão unicode, o padrao internacional

# Vale lembrar que primeiro vem todas as Maiusculas e depois as minusculas, dessa forma, Uma palavra com letra minuscula
# SEMPRE será maior que uma maiuscula
print(ord('a'))
print(ord('A'))



lista_string = ['chimito', 'Ariel', 'anakin', 'lili ', 'Supino', 'galadriel']


def ordenados(lista_string):
    menor = lista_string[0]
    for string in lista_string:
        if string.strip().lower() < menor.strip().lower():
            menor = string.strip()

    print(menor)


ordenados(lista_string)

