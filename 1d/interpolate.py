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

class HighOrder:
    def __init__(self, mesh, stencil, weighting, order):
        basis = TotalOrder(order)
        self.faceMoments = FaceMoments(mesh, basis)
        self.matrix = MomentsMatrix(mesh, basis, stencil, weighting)

    def __call__(self, rho, i):
        cp = self.matrix.coefficients(rho, i)
        return np.dot(cp, self.faceMoments.integrateOver(i))

