#!/usr/bin/python3
from mesh import *
from ddt import *
from div import *
from initial import *
from integration import *
from interpolate import *
from spacing import *

mesh = Mesh(nx=16, spacing=Uniform())

integration = Integration(
        mesh=mesh,
        Co=0.5,
        u=1,
        tracer=SineWave().tracer,
        ddt=RungeKutta(stages=2),
        interpolation=HighOrder(order=2, mesh=mesh, stencil=[-1, 0])
)
integration.integrate(endTime=1)
print(integration.l2error())

