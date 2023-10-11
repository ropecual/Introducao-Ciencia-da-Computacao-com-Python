class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b and self.a == self.c and self.b == self.c:
            return 'equilátero'
        else:
            if (self.a == self.b) or (self.a == self.c) or (self.b == self.c):
                return 'isósceles'
            else:
                return 'escaleno'

    def lados_organizados(self):
        lados = [self.a, self.b, self.c]
        return sorted(lados)

    def semelhantes(self, triangulo):
        lados_a = self.lados_organizados()
        lados_b = triangulo.lados_organizados()
        semelhante = True
        lista_divisao = []
        for i in range(len(lados_a)):
            lista_divisao.append(lados_a[i] / lados_b[i])

        for i in range(len(lista_divisao)):
            if i > 0:
                if lista_divisao[i] != lista_divisao[i - 1]:
                    semelhante = False

        return semelhante
