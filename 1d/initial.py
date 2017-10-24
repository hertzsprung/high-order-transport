import numpy as np

class SineWave:
    def tracer(self, mesh, i):
       return np.sin(2*np.pi*mesh.C[i])

class SineSquared:
    def tracer(self, mesh, i):
        return np.sin(2*np.pi*mesh.C[i])**2 if mesh.C[i] <= 0.5 else 0

class SquareWave:
    def tracer(self, mesh, i):
        C = mesh.C[i]
        return 1 if C > 0.1 and C < 0.4 else 0
