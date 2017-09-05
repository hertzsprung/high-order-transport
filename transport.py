#!/usr/bin/python3
from mesh import *
from ddt import *
from div import *
from initial import *
from interpolate import *
from simulation import *
from spacing import *
from stencil import *

mesh = Mesh(nx=16, spacing=Uniform())

simulation = Simulation(
        mesh=mesh,
        Co=0.5,
        u=1,
        tracer=SineWave().tracer,
        ddt=RungeKutta(stages=2),
        interpolation=HighOrder(mesh, Stencil([-1, 0]), order=2)
)

simulation.integrate(endTime=simulation.dt)
simulation.results[0].dumpTo('build/0.dat')
simulation.results[1].dumpTo('build/dt.dat')
simulation.numeric.dumpTo('build/1.dat')
print('l2error', simulation.l2error())

