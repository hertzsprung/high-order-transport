import numpy as np

class Stencil:
    def __init__(self, indices):
        self.indices = np.array(indices)

    def __len__(self):
        return len(self.indices)

    def __radd__(self, other):
        return other + self.indices
