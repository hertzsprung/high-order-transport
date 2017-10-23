import itertools
import math
import numpy as np

class Simplex:
    def __init__(self, a, b, c):
        self.a = np.array(a)
        self.b = np.array(b)
        self.c = np.array(c)

    def _moment(self, p, q, r, d):
        return self._detA()*np.sum([
            self._factorial_term(p, q, r, k_ij, d) * self._vertex_powers(k_ij) \
            for k_ij in self._k_ij_list(p, q, r)])

    def _detA(self):
        A = np.column_stack([self.a, self.b, self.c])
        return np.linalg.det(A)
    
    def _k_ij_list(self, p, q, r):
        p_exponents = self._vectors_summing_to(p)
        q_exponents = self._vectors_summing_to(q)
        r_exponents = self._vectors_summing_to(r)
        return [np.array(k_ij) for k_ij in \
                itertools.product(p_exponents, q_exponents, r_exponents)]

    def _vectors_summing_to(self, x):
        return [e for e in \
                itertools.product(range(x+1), repeat=3) if np.sum(e) == x]

    def _factorial_term(self, p, q, r, k_ij, dimensions):
        k = p + q + r
        return  math.factorial(p) * math.factorial(q) * math.factorial(r) * \
                np.prod([math.factorial(np.sum(k_ij[:,j])) for j in range(3)]) \
                / \
                (math.factorial(k+dimensions) * self._prod_factorial(k_ij))

    def _prod_factorial(self, k_ij):
        return np.prod([math.factorial(e) for e in k_ij.flat])
    
    def _vertex_powers(self, k_ij):
        return  self.a[0] ** k_ij[0, 0] * \
                self.a[1] ** k_ij[0, 1] * \
                self.a[2] ** k_ij[0, 2] * \
                self.b[0] ** k_ij[1, 0] * \
                self.b[1] ** k_ij[1, 1] * \
                self.b[2] ** k_ij[1, 2] * \
                self.c[0] ** k_ij[2, 0] * \
                self.c[1] ** k_ij[2, 1] * \
                self.c[2] ** k_ij[2, 2]
