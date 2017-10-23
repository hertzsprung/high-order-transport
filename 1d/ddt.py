class ForwardEuler:
    def __call__(self, rho, op, dt):
        return rho + dt*op(rho)

class RungeKutta2:
    def __init__(self, stages):
        self.stages = stages

    def __call__(self, rho, op, dt):
        rho_old = rho

        for stage in range(self.stages):
            rho = rho_old + 0.5*dt*(op(rho)+op(rho_old))

        return rho

class RungeKutta3:
    def __call__(self, rho, op, dt):
        rho_old = rho

        rho = rho_old + dt/3*op(rho)
        rho = rho_old + dt/2*op(rho)
        rho = rho_old + dt*op(rho)

        return rho

class RungeKutta4:
    def __call__(self, rho, op, dt):
        rho_old = rho

        k1 = op(rho)
        k2 = op(rho_old + dt/2*k1)
        k3 = op(rho_old + dt/2*k2)
        k4 = op(rho_old + dt*k3)
        rho = rho_old + dt/6*(k1 + 2*k2 + 2*k3 + k4)

        return rho
    
