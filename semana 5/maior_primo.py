def maior_primo(numero):
    i = 1
    count = 0
    while i < numero:
        if numero % i == 0:
            count += 1
        i += 1
        if count > 1:
            numero -= 1
            count = 0
            i = 1

    return numero
