from Bhaskara import Bhaskara
import pytest


# Fixture é um valor fixo para um conjunto de testes
# É usado muitas vezes para guardar um objeto que requer um pouco mais de trabalho para ser criado
# Para definir uma fixure, implementemos uma função que cria o objeto e a marcamos com o decorator @pytest.fixture

class TestBhaskara:

    @pytest.fixture
    def b(self):
        return Bhaskara()

    def testa_uma_raiz(self, b):
        assert b.calcula_raizes(1, 0, 0) == (1, 0)

    def testa_duas_raizes(self, b):
        assert b.calcula_raizes(1, -5, 6) == (2, 3, 2)

    def testa_zero_raizes(self, b):
        assert b.calcula_raizes(10, 10, 10) == (0)

    def testa_raiz_negativa(self):
        b = Bhaskara()
        assert b.calcula_raizes(10, 20, 10) == (1, -1)
