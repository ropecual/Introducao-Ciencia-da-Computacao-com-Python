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

    def retangulo(self):
        lados = self.lados_organizados()
        if (lados[0] ** 2 + lados[1] ** 2) == lados[2] ** 2:
            return True
        else:
            return False
