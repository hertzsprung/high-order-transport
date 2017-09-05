import numpy as np
from div import *
from mesh import *

class Simulation:
    def __init__(self, mesh, Co, u, tracer, ddt, interpolation):
        self.mesh = mesh
        self.tracer = tracer
        self.u = u
        self.dt = u*np.min(self.mesh.dx)*Co
        self.ddt = ddt
        self.div = Div(u, interpolation)
        self.results = []

    def integrate(self, endTime):
        rho = ScalarField.initialise(self.mesh, self.tracer)
        self.results.append(rho)
        rhoAnalytic = rho

        dts = 0
        t = 0
        while t < endTime:
            dts += 1
            rho = self.ddt(rho, -self.div, self.dt) 
            print("timesteps={dts}\tmin={min}\tmax={max}".format(
                dts=dts, min=rho.min(), max=rho.max()))
            self.results.append(rho)
            t += self.dt

        self.numeric = rho
        self.analytic = rhoAnalytic
        self.difference = rho - rhoAnalytic

    def l2error(self):
        differenceSquared = 0
        analyticSquared = 0

        for i in range(self.mesh.cells):
            differenceSquared += self.difference[i]**2*self.mesh.dx[i]
            analyticSquared += self.analytic[i]**2*self.mesh.dx[i]

        return np.sqrt(differenceSquared/analyticSquared) 

