import numpy as np

from basis import *
from moments import *

class Upwind:
    def __call__(self, rho, i):
        return rho[i-1]

class Linear:
    def __call__(self, rho, i):
        l = rho[i-1]
        r = rho[i]

        Cf = rho.mesh.faceCentre(i)

        distance_l = Cf - rho.mesh.cellCentre(i-1)
        distance_r = rho.mesh.cellCentre(i) - Cf

        if distance_l < 0:
            distance_l += 1

        if distance_r < 0:
            distance_r += 1

        distance_total = distance_l + distance_r

        weight_l = (distance_total - distance_l)/distance_total
        weight_r = (distance_total - distance_r)/distance_total

        return weight_l*l + weight_r*r

class PointwisePolynomial:
    def __init__(self, mesh, stencil, weighting, order):
        self.mesh = mesh
        self.stencil = stencil
        self.weighting = weighting
        self.Ainv = np.empty(self.mesh.cells, dtype='O')
        self.basis = TotalOrder(order)

        for i in range(mesh.cells):
            self.Ainv[i] = self.initialiseInverseMatrix(i)

    def initialiseInverseMatrix(self, index):
        A = np.empty((len(self.stencil), len(self.basis.terms)))

        cellCentres = self.stencil.relativeCellCentres(self.mesh, index)
        
        for row, i in enumerate(index + self.stencil.indices):
            for col, term in enumerate(self.basis.terms):
                A[row, col] = term(cellCentres[row])

        print('A', A)
        A = np.dot(self.weighting(index), A)
        print('A weighted', A)
        Ainv = np.linalg.pinv(A)
        Ainv = np.dot(Ainv, self.weighting(index))

        print('Ainv', Ainv)
        return Ainv

    def __call__(self, rho, i):
        stencilValues = rho[i + self.stencil]
        return np.dot(self.Ainv[i % self.mesh.cells][0], stencilValues)


class HighOrder:
    def __init__(self, mesh, stencil, weighting, order):
        basis = TotalOrder(order)
        self.faceMoments = FaceMoments(mesh, basis)
        self.matrix = MomentsMatrix(mesh, basis, stencil, weighting)

    def __call__(self, rho, i):
        cp = self.matrix.coefficients(rho, i)
        return np.dot(cp, self.faceMoments.integrateOver(i))

