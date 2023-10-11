def conta_letras(frase, contar="vogais"):
    count = 0
    if contar == 'vogais':
        for letra in frase:
            for char in letra:
                if char in 'AaEeIiOoUu':
                    count += 1
    if contar == 'consoantes':
        for letra in frase:
            for char in letra:
                if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
                    count += 1
    return count
