import numpy as np

class FaceMoments:
    def __init__(self, mesh, basis):
        self.basis = basis

    def integrateOver(self, i):
        return np.full(len(self.basis.terms), fill_value=1)

class MomentsMatrix:
    def __init__(self, mesh, basis, stencil):
        self.mesh = mesh
        self.basis = basis
        self.stencil = stencil
        self.Minv = np.empty(self.mesh.cells, dtype='O')

        for i in range(mesh.cells):
            self.Minv[i] = self.initialiseInverseMatrix(i)

    def initialiseInverseMatrix(self, index):
        M = np.empty((len(self.stencil), len(self.basis.terms)))
        
        for row, i in enumerate(index + self.stencil.indices):
            for col, term in enumerate(self.basis.terms):
                M[row,col] = term.integrate().evaluate(
                        self.mesh.faceCentre(i),
                        self.mesh.faceCentre(i+1),
                        self.mesh.cellCentre(i))
                M[row,col] /= self.mesh.dx[i % self.mesh.cells]

        print(M)
        print('cond', np.linalg.cond(M))

        return np.linalg.pinv(M)

    def coefficients(self, rho, i):
        stencilValues = rho[i + self.stencil]
#        print(self.Minv[i % self.mesh.cells])
#        print(np.sum(self.Minv[i % self.mesh.cells]))
        return np.dot(self.Minv[i % self.mesh.cells], stencilValues)
