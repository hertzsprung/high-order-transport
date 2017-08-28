import numpy as np

class Uniform:
    def __call__(self, nx):
        return np.full(nx, fill_value=1/nx)

class SmoothNonuniform:
    def __call__(self, nx, m=4, c=1):
        dx = np.array([float(m*x/nx+c) for x in range(nx)])
        return np.multiply(dx, 1/np.sum(dx))
