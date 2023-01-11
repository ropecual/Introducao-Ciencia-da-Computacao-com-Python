n = 5
m = 3

def computador_escolhe_jogada(n, m):
    count = 0
    while n % (m + 1) != 0:
        count += 1
        n -= 1
    if count == 0:
        return m
    elif count > 0 and count <= m:
        return n - (n - count)
    else:
        return m



a = computador_escolhe_jogada(n,m)

print(a)