#!/usr/bin/env python3
'''
An implementation of https://doi.org/10.1109/ICIP.2001.958220 for tetrahedra
'''

import numpy as np
import math
import itertools

class Tetrahedron:
    def __init__(self, a, b, c):
        self.a = np.array(a)
        self.b = np.array(b)
        self.c = np.array(c)

    def volume(self):
        # https://en.wikipedia.org/wiki/Tetrahedron#Volume
        return np.linalg.norm(np.dot(self.a, np.cross(self.b, self.c)))/6

    def moment(self, p, q, r):
        return self._detA() * np.sum([
            self._factorial_term(p, q, r, k_ij) * self._vertex_powers(k_ij) \
            for k_ij in self._k_ij_list(p, q, r)])

    def _detA(self):
        A = np.column_stack([self.a, self.b, self.c])
        return np.linalg.det(A)
    
    def _k_ij_list(self, p, q, r):
        p_exponents = self._vectors_summing_to(p)
        q_exponents = self._vectors_summing_to(q)
        r_exponents = self._vectors_summing_to(r)
        return [np.array(k_ij) for k_ij in itertools.product(p_exponents, q_exponents, r_exponents)]

    def _vectors_summing_to(self, x):
        return [e for e in itertools.product(range(x+1), repeat=3) if np.sum(e) == x]

    def _factorial_term(self, p, q, r, k_ij):
        k = p + q + r
        return  math.factorial(p) * math.factorial(q) * math.factorial(r) * \
                np.prod([math.factorial(np.sum(k_ij[:,j])) for j in range(3)]) \
                / \
                (math.factorial(k+3) * np.prod([math.factorial(e) for e in k_ij.flat]))
    
    def _vertex_powers(self, k_ij):
        return  self.a[0] ** k_ij[0, 0] * self.a[1] ** k_ij[0, 1] * self.a[2] ** k_ij[0, 2] * \
                self.b[0] ** k_ij[1, 0] * self.b[1] ** k_ij[1, 1] * self.b[2] ** k_ij[1, 2] * \
                self.c[0] ** k_ij[2, 0] * self.c[1] ** k_ij[2, 1] * self.c[2] ** k_ij[2, 2]

    def __str__(self):
        return 'Tetrahedron([0 0 0], ' + str(self.a) + ', ' + \
                str(self.b) + ', ' + str(self.c) + ')'

if __name__ == '__main__':
    t = Tetrahedron(
        [2, 3, 1],
        [1, 1, 4],
        [4, 4, 2])
    print(t)

    print('volume', t.volume())
    print('zeroth moment', t.moment(0, 0, 0))
    print('(0 2 0)th moment', t.moment(0, 2, 0))
