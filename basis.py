import sympy as sp

class TotalOrder:
    def __init__(self, order):
        self.terms = [Term(o) for o in range(order)]

class Term:
    x = sp.Symbol('x')

    def __init__(self, exponent):
        self.exponent = exponent

    def integrate(self, leftFace, rightFace):
        return sp.integrate(
                Term.x**self.exponent,
                (Term.x, leftFace, rightFace))

