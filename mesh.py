import numpy as np

class Mesh:
    def __init__(self, nx, spacer):
        self.nx = nx
        self.dx = spacer(nx)
        self.Cf = np.append(0, np.cumsum(self.dx))
        self.C = [0.5*(l+r) for l, r in zip(self.Cf[:-1], self.Cf[1:])]
        self.cells = len(self.C)

    def cellCentre(self, i):
        return self.C[i % self.nx]

    def faceCentre(self, i):
        return self.Cf[i % (self.nx+1)]

class ScalarField:
    def __init__(self, mesh, rho):
        self.mesh = mesh
        self.rho = rho

    @classmethod
    def initialise(cls, mesh, initialiser):
        rho = np.empty(len(mesh.C))
        for i in range(mesh.cells):
            rho[i] = initialiser(mesh, i)

        return cls(mesh, rho)

    def __getitem__(self, i):
        return self.rho[i % self.mesh.nx]

    def __add__(self, other):
        return ScalarField(self.mesh, other + self.rho)

    def __sub__(self, other):
        return ScalarField(self.mesh, self + (-other))

    def __rmul__(self, other):
        return other*self.rho

    def __neg__(self):
        return ScalarField(self.mesh, -self.rho)

    def dumpTo(self, filename):
        with open(filename, 'w') as file:
            for C, rho in zip(self.mesh.C, self.rho):
                print(C, rho, file=file)

