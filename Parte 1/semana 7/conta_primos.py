def primo(num):
    i = 1
    count = 0
    if num == 1:
        return False
    while i < int(num):
        if int(num) % i == 0:
            count += 1
        i += 1
    if count > 1:
        return False
    else:
        return True


def n_primos(n):
    i = 1
    count = 0
    while i <= n:
        if primo(i):
            count += 1
        i += 1
    return count

