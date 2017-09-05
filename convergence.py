#!/usr/bin/python3
import numpy as np

from mesh import *
from ddt import *
from div import *
from initial import *
from interpolate import *
from simulation import *
from spacing import *
from stencil import *

def orderOfConvergence(nxs, initialiser):
    dxs = []
    errors = []

    for nx in nxs:
        print(nx)
        simulation = initialiser(nx)
        simulation.integrate(endTime=1)
        dxs += [np.min(simulation.mesh.dx)]
        errors += [simulation.l2error()]

    A = np.vstack([np.log(dxs), np.ones(len(dxs))]).T
    m, c = np.linalg.lstsq(A, np.log(errors))[0]
    return m

def initialiser(nx):
    mesh = Mesh(nx, Uniform())
    return Simulation(
            mesh=mesh,
            Co=0.5,
            u=1,
            tracer=SineWave().tracer,
            ddt=RungeKutta(stages=2),
            interpolation=HighOrder(mesh, Stencil([-1, 0]), order=2)
    )

nxs = reversed([2**n for n in range(4,9)])
print("convergence", orderOfConvergence(nxs, initialiser))
