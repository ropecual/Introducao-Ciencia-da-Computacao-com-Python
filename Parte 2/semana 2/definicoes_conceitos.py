# Inversao de valores


a = 10
b = 20

print(a)
print(b)
a, b = b, a

print(a)
print(b)

print('---------')
x = 10
y = 12

x, y = y, x

print(x)
print(y)

print('---------')
x = 10
x += 10
x /= 2
x //= 3
x %= 2
x *= 9
print(x)

print('---------')


def calculo(x, y=10, z=5):
    return x + y * z


print(calculo(1, 2, 3))

print('---------')


def horario_em_segundos(h, m, s):
    assert h >= 0 and m >= 0 and s >= 0
    return h * 3600 + m * 60 + s

print(horario_em_segundos(-1,20,30))
