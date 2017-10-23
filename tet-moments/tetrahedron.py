import math
import numpy as np
from simplex import Simplex

class Tetrahedron(Simplex):
    def volume(self):
        # https://en.wikipedia.org/wiki/Tetrahedron#Volume
        return np.linalg.norm(np.dot(self.a, np.cross(self.b, self.c)))/6

    def moment(self, p, q, r):
        return self._moment(p, q, r, d=3)

    def __str__(self):
        return 'Tetrahedron([0 0 0], ' + str(self.a) + ', ' + \
                str(self.b) + ', ' + str(self.c) + ')'
