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

        faceCentres = self.stencil.relativeFaceCentres(self.mesh, index)
        
        for row, i in enumerate(index + self.stencil.indices):
            for col, term in enumerate(self.basis.terms):
                M[row,col] = term.integrate(
                        faceCentres[row], faceCentres[row+1])
                M[row,col] /= self.mesh.dx[i % self.mesh.cells]

        print('M', M)
        print('Minv', np.linalg.pinv(M))
        print('sum(Minv)', np.sum(np.linalg.pinv(M)))
        print('cond(M)', np.linalg.cond(M))

        return np.linalg.pinv(M)

    def coefficients(self, rho, i):
        stencilValues = rho[i + self.stencil]
        return np.dot(self.Minv[i % self.mesh.cells], stencilValues)
