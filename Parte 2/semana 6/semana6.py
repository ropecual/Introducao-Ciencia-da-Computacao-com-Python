# Muitos problemas contem, dentro de si, problemas menores
#  que sao similares ao problema maior

# Esses problemas tem uma estrutura RECURSIVA

# Podemos aplicar um algoritmo recursivo para resolve-los

# Se o tamanho do problema for pequeno, resolva-o diretamente,
# Senao
# Reduza-o a uma instancia menor do mesmo problema
# Aplique o algoritmo (recursivamente) a instancia menor
# Volte a instancia original


# Exemplos de recursivos
# Fatorial, Fibonacci, Busca Binaria, MergeSort
import pytest

def fatorial(n):
    if n < 1:  # Base da recursao
        return 1
    else:
        return n * fatorial(n - 1)  # Chamada Recursiva





@pytest.mark.parametrize("entrada, esperado", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
])
def testa_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado


def fibonacci(n):
    if n < 2:  # Base da recursao
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Chamada Recursiva


@pytest.mark.parametrize("entrada, esperado", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13)
])
def testa_fibonacci(entrada, esperado):
    assert fibonacci(entrada) == esperado


def busca_binaria_recursiva(lista, elemento, min=0, max=None):
    if max == None:
        max = len(lista) - 1

    if max < min:
        return False
    else:
        meio = min + (max - min) // 2

    if lista[meio] > elemento:
        return busca_binaria_recursiva(lista, elemento, min, meio - 1)
    elif lista[meio] < elemento:
        return busca_binaria_recursiva(lista, elemento, meio + 1, max)
    else:
        return meio


a = [10, 20, 30, 40, 50, 60]
@pytest.mark.parametrize("lista,valor, esperado", [
    (a, 10, 0),
    (a, 20, 1),
    (a, 30, 2),
    (a, 40, 3),
    (a, 50, 4),
    (a, 60, 5),
    (a, 70, False),
    (a, 15, False),
    (a, -10, False),

])
def test_busca_binaria_recursiva(lista, valor, esperado):
    assert busca_binaria_recursiva(lista, valor) == esperado



def elefantes(n):
    if n < 0:
        return ""
    if n == 1:
        return "Um elefante incomoda muita gente\n"
    else:
        frase1 = elefantes(n - 1) + str(n) + " elefantes " + "incomodam " * n + "muito mais\n"
        frase2 = str(n) + " elefantes " + "incomodam muita gente\n"
        return frase1 + frase2


#print(elefantes(4))
