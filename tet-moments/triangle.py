import numpy as np
import math
from simplex import Simplex

class Triangle(Simplex):
    def area(self):
        # https://math.stackexchange.com/a/516223/89878
        return 0.5 * self._detA()

    def moment(self, p, q, r):
        return self._moment(p, q, r, d=2)

    def __str__(self):
        return 'Triangle(' + str(self.a) + ', ' + \
                str(self.b) + ', ' + str(self.c) + ')'
