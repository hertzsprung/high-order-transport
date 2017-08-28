#!/usr/bin/python3
import numpy as np

class Mesh:
    def __init__(self, nx):
        self.nx = nx
        self.dx = np.full(nx, fill_value=1/nx)
        self.Cf = np.append(0, np.cumsum(self.dx))
        self.C = [0.5*(l+r) for l, r in zip(self.Cf[:-1], self.Cf[1:])]
        self.cells = len(self.C)

    def faceCentre(self, i):
        return self.Cf[i % self.nx]

class ScalarField:
    def __init__(self, mesh, rho):
        self.mesh = mesh
        self.rho = rho

    @classmethod
    def initialise(cls, mesh, initialiser):
        rho = np.empty(len(mesh.C))
        for i in range(mesh.cells):
            rho[i] = initialiser(mesh, i)

        return cls(mesh, rho)

    def __getitem__(self, i):
        return self.rho[i % self.mesh.nx]

    def __add__(self, other):
        return ScalarField(mesh, self.rho + other)

    def __rmul__(self, other):
        return other*self.rho

    def dumpTo(self, filename):
        with open(filename, 'w') as file:
            for C, rho in zip(self.mesh.C, self.rho):
                print(C, rho, file=file)

class SineWave:
    def tracer(self, mesh, i):
       return np.sin(2*np.pi*mesh.C[i])

class ForwardEuler:
    def __init__(self, dt):
        self.dt = dt

    def __call__(self, rho, op):
        return rho + dt*op(rho)

class Div:
    def __init__(self, interpolation):
        self.interpolation = interpolation

    def __call__(self, rho):
        def initialiser(mesh, i):
            l = self.interpolation(rho, i, mesh.faceCentre(i))
            r = self.interpolation(rho, i+1, mesh.faceCentre(i+1))

            return (r-l)/mesh.dx[i]

        return ScalarField.initialise(mesh, initialiser)

class Upwind:
    def __call__(self, rho, i, position):
        return rho[i]


mesh = Mesh(nx=32)
rho = ScalarField.initialise(mesh, SineWave().tracer)

t = 0
endTime = 1
u = 1
dt = u*np.min(mesh.dx)/2
print('dt', dt)
print('Co', u*dt/np.min(mesh.dx))

ddt = ForwardEuler(dt)
interpolation = Upwind()
div = Div(interpolation)
rho.dumpTo('build/0.dat')

while t < endTime:
    rho = ddt(rho, div) 
    t += dt
    rho.dumpTo('build/{t}.dat'.format(t=t))
    print(t)

