def MinMax(temperaturas):
    print("A menor temperatura do mês foi:", minima(temperaturas), "C")
    print("A menor temperatura do mês foi:", maxima(temperaturas), "C")


def minima(temps):
    min = temps[0]
    i = 0
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i += 1
    return min


def maxima(temps):
    max = temps[0]
    i = 0
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i += 1
    return max


lista = [2, 4, 2, 2, 3, 3, 1,5,10,-8,20,15,2,-4,-3,10,2]

MinMax(lista)