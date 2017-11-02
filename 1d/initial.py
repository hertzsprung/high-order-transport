import numpy as np

class Gaussian:
    def tracer(self, mesh, i, width=80, centre=0.5):
        return np.exp(-width*(mesh.C[i]-centre)**2)

class SineWave:
    def tracer(self, mesh, i):
       return np.sin(2*np.pi*mesh.C[i])

class TruncatedSineWave:
    def tracer(self, mesh, i):
        return np.sin(2*np.pi*mesh.C[i]) if mesh.C[i] <= 0.5 else 0

class SquareWave:
    def tracer(self, mesh, i):
        C = mesh.C[i]
        return 1 if C > 0.1 and C < 0.4 else 0
