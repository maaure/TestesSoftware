class Triangulo:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def validar_forma(self):
        """
        Verifica se os comprimentos dos lados formam um triângulo.
        """
        a = self.a
        b = self.b
        c = self.c
        return a > 0 and b > 0 and c > 0 and (a < b + c and b < a + c and c < a + b)

    def eh_equilatero(self):
        """
        Verifica se o triângulo é equilátero (três lados iguais).
        """
        return self.validar_forma() and self.a == self.b == self.c

    def eh_escaleno(self):
        """
        Verifica se o triângulo é escaleno (três lados diferentes).
        """
        return self.validar_forma() and self.a != self.b and self.b != self.c and self.c != self.a

    def eh_isosceles(self):
        """
        Verifica se o triângulo é isósceles (dois lados iguais).
        """
        return not self.eh_escaleno()
