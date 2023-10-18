def fibonacci(n):
    if n < 2:  # Base da recursao
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Chamada Recursiva
