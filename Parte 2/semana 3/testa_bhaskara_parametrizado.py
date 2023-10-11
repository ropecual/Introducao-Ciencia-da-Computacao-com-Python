from Bhaskara import Bhaskara
import pytest


class TestBhaskara:

    @pytest.fixture
    def b(self):
        return Bhaskara()

    # É possível criar listas de listas de saídas para facilitar os calculos
    @pytest.mark.parametrize("entrada1,entrada2,entrada3, saidas", [
        # Uma única raiz, sendo 0 o resultado
        (1, 0, 0, (1, 0)),
        # Duas raizes, sendo 3 e 2 os resultados
        (1, -5, 6, (2, 3, 2)),
        # Nenhuma raiz
        (10, 10, 10, 0),
        # Uma única raiz negativa
        (10, 20, 10, (1, -1))
    ])
    def testa_raizes(self, b, entrada1, entrada2, entrada3, saidas):
        assert b.calcula_raizes(entrada1, entrada2, entrada3) == saidas
