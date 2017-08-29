#!/usr/bin/python3
import numpy as np

from mesh import *
from ddt import *
from div import *
from initial import *
from integration import *
from interpolate import *
from spacing import *

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
