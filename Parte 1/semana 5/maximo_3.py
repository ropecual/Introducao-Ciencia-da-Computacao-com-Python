def maximo_2(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return x


def maximo(x, y, z):
    if z > maximo_2(x, y):
        return z
    else:
        return maximo_2(x, y)
