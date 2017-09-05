import numpy as np

class Stencil:
    def __init__(self, indices):
        self.indices = np.array(indices)

    def cellCentres(self, mesh, index):
        origin = mesh.cellCentre(index)

        Cs = []

        for i in self.indices:
            C = mesh.cellCentre(index + i)
            if i < 0 and C > origin:
                C -= 1

            if i > 0 and C < origin:
                C += 1

            Cs += [C]

        return np.array(Cs)

    def relativeFaceCentres(self, mesh, index):
        origin = mesh.faceCentre(index)

        Cfs = []

        for i in np.append(self.indices, self.indices[-1]+1):
            Cf = mesh.faceCentre(index + i)
            if i < 0 and Cf > origin:
                Cf -= 1

            if i > 0 and Cf < origin:
                Cf += 1

            Cfs += [Cf]

        return np.array(Cfs) - origin

    def __len__(self):
        return len(self.indices)

    def __radd__(self, other):
        return other + self.indices
