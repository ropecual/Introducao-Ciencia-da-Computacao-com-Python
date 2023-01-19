largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

altura_inicial = 1
largura_inicial = 1



while altura_inicial <= altura:
    while largura_inicial <= largura:
        print("#", end="")
        largura_inicial += 1
    largura_inicial = 1
    altura_inicial += 1
    print()
