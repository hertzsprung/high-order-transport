#!/usr/bin/python3
import numpy as np
import os

from convergence import *
from ddt import *
from div import *
from initial import *
from interpolate import *
from mesh import *
from simulation import *
from spacing import *
from stencil import *
from weighting import *

class Initialiser:
    def __init__(self, stencil, order):
        self.stencil = stencil
        self.order = order

    def __call__(self, nx):
        mesh = Mesh(nx, Uniform())
        return Simulation(
                mesh=mesh,
                Co=0.5,
                u=1,
                tracer=CosSquared().tracer,
                ddt=RungeKutta(stages=2),
                interpolation=HighOrder(
                    mesh,
                    self.stencil,
                    InverseDistanceWeighting(mesh, self.stencil),
                    self.order)
        )

initialisers = [
        Initialiser(Stencil([-2, -1, 0]), 1),
        Initialiser(Stencil([-2, -1, 0]), 2),
        Initialiser(Stencil([-2, -1, 0]), 3),
        Initialiser(Stencil([-3, -2, -1, 0]), 2),
        Initialiser(Stencil([-3, -2, -1, 0]), 3),
]

for initialiser in initialisers:
    convergence = Convergence(
            [2**n for n in range(4,8)],
            initialiser)

    print(
            'order', initialiser.order,
            'stencil', initialiser.stencil,
            'convergence', convergence.order()
    )

    convergence.dumpTo(
            os.path.join('build/convergence.order{order}.stencil{stencil}.dat'.format(
                order=initialiser.order,
                stencil=len(initialiser.stencil))))

