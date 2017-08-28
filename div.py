from mesh import *

class Div:
    def __init__(self, u, interpolation):
        self.u = u
        self.interpolation = interpolation

    def __call__(self, rho):
        def initialiser(mesh, i):
            l = self.interpolation(rho, i, mesh.faceCentre(i))
            r = self.interpolation(rho, i+1, mesh.faceCentre(i+1))

            return self.u*(r-l)/mesh.dx[i]

        return ScalarField.initialise(rho.mesh, initialiser)

    def __neg__(self):
        return lambda rho: -self(rho)

