#!/usr/bin/python3
import numpy as np

from mesh import *
from ddt import *
from div import *
from interpolate import *

class SineWave:
    def tracer(self, mesh, i):
       return np.sin(2*np.pi*mesh.C[i])

class Integration:
    def __init__(self, nx, Co, u, tracer, ddt, interpolation):
        self.mesh = Mesh(nx)
        self.tracer = tracer
        self.u = u
        self.dt = u*np.min(self.mesh.dx)*Co
        self.ddt = ddt
        self.div = Div(u, interpolation)

    def integrate(self, endTime):
        rho = ScalarField.initialise(self.mesh, self.tracer)
        rhoAnalytic = rho
        rho.dumpTo('build/0.dat')

        t = 0
        while t < endTime:
            rho = self.ddt(rho, -self.div, self.dt) 
            t += self.dt
            rho.dumpTo('build/{t}.dat'.format(t=t))

        self.numeric = rho
        self.analytic = rhoAnalytic
        self.difference = rho - rhoAnalytic

        self.difference.dumpTo('build/{t}.diff.dat'.format(t=t))

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
        integration = Integration(
                nx=nx,
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

print("convergence", orderOfConvergence(nxs=[2**n for n in range(4,9)]))
