import numpy as np

class Convergence:
    def __init__(self, nxs, initialiser):
        self.nxs = nxs
        self.initialiser = initialiser
        self.simulations = []
        self.dxs = []
        self.errors = []

    def order(self):
        for nx in self.nxs:
            print('nx', nx)
            simulation = self.initialiser(nx)
            simulation.integrate(endTime=1)

            self.simulations += [simulation]
            self.dxs += [np.min(simulation.mesh.dx)]
            self.errors += [simulation.l2error()]

        A = np.vstack([np.log(self.dxs), np.ones(len(self.dxs))]).T
        m, c = np.linalg.lstsq(A, np.log(self.errors))[0]
        return m

    def dumpTo(self, filename):
        with open(filename, 'w') as file:
            for dx, error in zip(self.dxs, self.errors):
                print(dx, error, file=file)
