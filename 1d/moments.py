import numpy as np

class FaceMoments:
    def __init__(self, mesh, basis):
        self.basis = basis

    def integrateOver(self, i):
        faceMoments = np.zeros(len(self.basis.terms))
        faceMoments[0] = 1
        return faceMoments

class MomentsMatrix:
    def __init__(self, mesh, basis, stencil, weighting):
        self.mesh = mesh
        self.basis = basis
        self.stencil = stencil
        self.weighting = weighting
        self.Ainv = np.empty(self.mesh.cells, dtype='O')

        for i in range(mesh.cells):
            self.Ainv[i] = self.initialiseInverseMatrix(i)

    def initialiseInverseMatrix(self, index):
        A = np.empty((len(self.stencil), len(self.basis.terms)))

        faceCentres = self.stencil.relativeFaceCentres(self.mesh, index)
        
        for row, i in enumerate(index + self.stencil.indices):
            for col, term in enumerate(self.basis.terms):
                A[row,col] = term.integrate(
                        faceCentres[row], faceCentres[row+1])
                A[row,col] /= self.mesh.dx[i % self.mesh.cells]

        print()
        print('Moments matrix for cell {i}'.format(i=index))
        print('A', A)
        A = np.dot(self.weighting(index), A)
        print('A weighted', A)
        Ainv = np.linalg.pinv(A)
        Ainv = np.dot(Ainv, self.weighting(index))

        print('Ainv', Ainv)
        print('sum(Ainv)', np.sum(Ainv))
        print('cond(A)', np.linalg.cond(A))

        return Ainv

    def coefficients(self, rho, i):
        stencilValues = rho[i + self.stencil]
        return np.dot(self.Ainv[i % self.mesh.cells], stencilValues)
