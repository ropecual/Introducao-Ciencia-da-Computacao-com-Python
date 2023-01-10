numero = int(input("Digite o valor de n: "))

if numero >= 0:
    numero *= 2
    i = 1

    while i <= numero:
        if i % 2 != 0:
            print(i)
        i += 1
