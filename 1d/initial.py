import numpy as np

class SineWave:
    def tracer(self, mesh, i):
       return np.sin(2*np.pi*mesh.C[i])

class CosSquared:
    def tracer(self, mesh, i):
        return np.cos(np.pi*mesh.C[i])**2
