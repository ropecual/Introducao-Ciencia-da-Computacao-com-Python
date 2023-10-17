from bubblesort import Ordenador
import pytest
import random


class TestaOrdenador:
    @pytest.fixture
    def o(self):
        return Ordenador()

    @pytest.fixture
    def l_aleatoria(self):
        lista = []
        for i in range(5000):
            lista.append(random.randint(-10000, 10000))
        return lista

    def esta_ordenada(self, l):
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                return False

        return True

    def test_bolha(self, o, l_aleatoria):
        assert self.esta_ordenada(o.bolha(l_aleatoria))

    def test_bolha_melhorada(self, o, l_aleatoria):
        assert self.esta_ordenada(o.bolha_melhorada(l_aleatoria))

    def test_selecao_direta(self, o, l_aleatoria):
        assert self.esta_ordenada(o.selecao_direta(l_aleatoria))

    def test_insercao(self, o, l_aleatoria):
        assert self.esta_ordenada(o.insercao(l_aleatoria))