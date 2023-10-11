def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=" ")
        a, b = b, a + b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b

    return result


# Significa que estou executando o programa como SCRIPTS, caso o nome seja main, no caso sem importanção;
# se não for main, significa que estou importando o mesmo
if __name__ == "__main__":
    import sys

    fib(int(sys.argv[1]))
