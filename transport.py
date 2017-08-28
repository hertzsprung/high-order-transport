#!/usr/bin/python3
import numpy as np

from mesh import *
from ddt import *
from div import *
from interpolate import *
from spacer import *

class SineWave:
    def tracer(self, mesh, i):
       return np.sin(2*np.pi*mesh.C[i])

class Integration:
    def __init__(self, mesh, Co, u, tracer, ddt, interpolation):
        self.mesh = mesh
        self.tracer = tracer
        self.u = u
        self.dt = u*np.min(self.mesh.dx)*Co
        self.ddt = ddt
        self.div = Div(u, interpolation)

    def integrate(self, endTime):
        rho = ScalarField.initialise(self.mesh, self.tracer)
        rhoAnalytic = rho

        t = 0
        while t < endTime:
            rho.dumpTo('build/{t}.dat'.format(t=t))
            rho = self.ddt(rho, -self.div, self.dt) 
            t += self.dt

        self.numeric = rho
        self.analytic = rhoAnalytic
        self.difference = rho - rhoAnalytic

        rho.dumpTo('build/1.dat')
        self.difference.dumpTo('build/1.diff.dat')

    def l2error(self):
        differenceSquared = 0
        analyticSquared = 0

        for i in range(self.mesh.cells):
            differenceSquared += self.difference[i]**2*self.mesh.dx[i]
            analyticSquared += self.analytic[i]**2*self.mesh.dx[i]

        return np.sqrt(differenceSquared/analyticSquared) 

def orderOfConvergence(nxs):
    dxs = []
    errors = []

    for nx in nxs:
        print(nx)
        integration = Integration(
                mesh=Mesh(nx, SmoothNonuniform()),
                Co=0.5,
                u=1,
                tracer=SineWave().tracer,
                ddt=RungeKutta(stages=2),
                interpolation=Linear()
        )
        integration.integrate(endTime=1)
        dxs += [np.min(integration.mesh.dx)]
        errors += [integration.l2error()]

    A = np.vstack([np.log(dxs), np.ones(len(dxs))]).T
    m, c = np.linalg.lstsq(A, np.log(errors))[0]
    return m

print("convergence", orderOfConvergence(nxs=reversed([2**n for n in range(4,9)])))
