def fatorial(n):
    if n < 1:  # Base da recursao
        return 1
    else:
        return n * fatorial(n - 1)  # Chamada Recursiva
