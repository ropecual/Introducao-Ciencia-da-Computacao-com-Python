for i in range(0, 20, 3):
    print(i)


for n in range(20, 0, -5):
    print(n)


frutas = ["Banana","Maçã","Pêra"]


for fruta in frutas:
    print(fruta)

animais = ["gato", "cachorro", "papagaio", "arara", "jacaré"]
for x in range(len(animais)):
    print("--> ", animais[x])


#usar isso no BS4
for x in range(len(animais)):
    print("-1->", animais[x])


for i in range(16,4,-3):
    print(i)



pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
for x in range(len(pares)):
    print(x, end=" ")

print()

for i in range(0,50,5):
    print(i, end=" ")

print()

pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
for x in range(5,10):
    print(pares[x], end=" ")



print()


valores = []
for i in range(1, 10):
    if i % 2 == 0:
        valores.append(i)

for i in range(len(valores)):
    print(valores[i])


print()


valores = []
for i in range(2, 10,2):
    valores.append(i)

for i in range(len(valores)):
    print(valores[i])


pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

pares[2:4]
print(pares[2:4])



lista1 = ["Amarelo", "Vermelho", "Verde"]

lista2 = lista1

lista3 = lista1[:2]

print(lista3)


# Pertinência
print("Rosa" in lista1)
print("Verde" in lista1)

# Concatenação
lista_concatenada = lista1 + pares
print(lista_concatenada)

# Remoção
del pares[2:10]
print(pares)



alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


letras = alfabeto[13:2]

print(letras)
print(len(alfabeto))

# Cria uma referencia
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = carnes
carnes2.append("ponta de alcatra")


print(carnes)
print(carnes2)
print()

carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = []
for cns in carnes:
    carnes2.append(cns)
carnes2.append("ponta de alcatra")

print(carnes)
print(carnes2)
print()
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = carnes[:]
carnes2.append("ponta de alcatra")

print(carnes)
print(carnes2)
print()


carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
x = carnes
del (x[-1])

print(carnes)
print(x)
print()