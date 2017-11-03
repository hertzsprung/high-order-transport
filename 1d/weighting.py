import numpy as np

class UniformWeighting:
    def __init__(self, stencil):
        self.stencil = stencil

    def __call__(self, i):
        return np.diag(np.ones(len(self.stencil)))

class InverseDistanceWeighting:
    def __init__(self, mesh, stencil):
        self.mesh = mesh
        self.W = np.empty(mesh.cells, dtype='O')

        for i in range(mesh.cells):
            w = []
            cellCentres = stencil.cellCentres(mesh, i)
            cellCentres -= mesh.cellCentre(i-1)

            for cellCentre, stencilI in zip(
                    cellCentres, i + stencil.indices):
                distance = abs(cellCentre)/mesh.dx[stencilI % mesh.cells]

                w += [1 if distance < 0.5 else (2*distance)**-5]

            print('weightings', i, w)
            self.W[i] = np.diag(w)

    def __call__(self, i):
        return self.W[i % self.mesh.cells]
                
