def maiusculas(frase):
    max = ""
    for letra in frase:
        # Como o a minusculo na tabela ASCII, em DEC é 97, faço uma condicional, o que for menor que esse
        # número, é maiuscula
        if 90 >= ord(str(letra)) >= 65:
            max = max + letra
    return max
