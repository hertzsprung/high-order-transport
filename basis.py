class TotalOrder:
    def __init__(self, order):
        self.terms = []
        for o in range(order):
            self.terms += [Term(o)]    

    def __repr__(self):
        return ' + '.join([t.formatCoefficient() + ' c_' + str(i+1) + ' ' + t.formatX() for i, t in enumerate(self.terms)])

class Term:
    def __init__(self, exponent, coefficient=1):
        self.coefficient = coefficient
        self.exponent = exponent

    def integrate(self):
        return Term(self.exponent+1, self.coefficient/(self.exponent+1))

    def evaluate(self, leftFace, rightFace, cellCentre):
        if rightFace < leftFace:
            rightFace += 1
        def t(x):
            return self.coefficient * (x-cellCentre)**self.exponent

        return t(rightFace) - t(leftFace)

    def __repr__(self):
        return self.formatCoefficient() + ' ' + self.formatX()

    def formatCoefficient(self):
        if self.coefficient == 1:
            return ''
        else:
            return str(self.coefficient)

    def formatX(self):
        if self.exponent == 0:
            return ''
        elif self.exponent == 1:
            return 'x'
        else:
            return 'x^' + str(self.exponent)
