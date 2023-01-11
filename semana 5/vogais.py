def vogal(letra):
    vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    i = 0
    count = 0
    while i < len(vogais):
        if letra == vogais[i]:
            count += 1
        i += 1
    if count > 0:
        return True
    else:
        return False
