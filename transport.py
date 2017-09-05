#!/usr/bin/python3
from mesh import *
from ddt import *
from div import *
from initial import *
from integration import *
from interpolate import *
from spacing import *
from stencil import *

mesh = Mesh(nx=16, spacing=Uniform())

integration = Integration(
        mesh=mesh,
        Co=0.5,
        u=1,
        tracer=SineWave().tracer,
        ddt=RungeKutta(stages=2),
        interpolation=HighOrder(mesh, Stencil([-1, 0]), order=2)
)

integration.integrate(endTime=integration.dt)
integration.results[0].dumpTo('build/0.dat')
integration.results[1].dumpTo('build/dt.dat')
integration.numeric.dumpTo('build/1.dat')
print('l2error', integration.l2error())

