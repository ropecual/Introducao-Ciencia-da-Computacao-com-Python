import math


class Bhaskara:
    def delta(self, a, b, c):
        return b ** 2 - 4 * a * c

    def calcula_raizes(self, a, b, c):
        d = self.delta(a, b, c)
        if d == 0:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            return 1, raiz1
        else:
            if d < 0:
                return 0
            else:
                raiz1 = (-b + math.sqrt(d)) / (2 * a)
                raiz2 = (-b - math.sqrt(d)) / (2 * a)
                return 2, raiz1, raiz2

    def main(self):
        a_digitado = float(input("A: "))
        b_digitado = float(input("B: "))
        c_digitado = float(input("C: "))
        print(self.calcula_raizes(a_digitado, b_digitado, c_digitado))


