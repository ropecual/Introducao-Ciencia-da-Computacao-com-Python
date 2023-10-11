class Pato:
    pass


pato = Pato()
patinho = Pato()

if pato == patinho:
    print("Estamos no mesmo endereço!")
else:
    print("Estamos em endereços diferentes!")


# Método especial __init__
# Conhecido como método CONSTRUTOR
# É chamado automaticamente pelo interpretador quando os objetos são criados

# O self representa o PROPRIO OBJETO

class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor


meu_carro = Carro('ford ka', 2013, 'branco')

print(meu_carro.modelo)
print(meu_carro.ano)
print(meu_carro.cor)


class Cafeteira:
    def __init__(self, marca, tipo, tamanho, cor):
        self.marca = marca
        self.tipo = tipo
        self.tamnho = tamanho
        self.cor = cor


class Cachorro:
    def __init__(self, raca, idade, nome, cor):
        self.raca = raca
        self.idade = idade
        self.nome = nome
        self.cor = cor


rex = Cachorro('vira-lata', 2, 'Bobby', 'marrom')

print(rex.idade > 2)
print(rex.idade == '2')
print('vira-lata' == rex.raca)
print(rex.nome == 'rex')


class Lista:
    def append(self, elemento):
        return 'Oops! Este objeto não é uma lista'


lista = []

a = Lista()
b = a.append(7)
lista.append(b)


print(a)
print(b)
print(lista)