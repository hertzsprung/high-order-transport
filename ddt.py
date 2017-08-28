class ForwardEuler:
    def __call__(self, rho, op, dt):
        return rho + dt*op(rho)

class RungeKutta:
    def __init__(self, stages):
        self.stages = stages

    def __call__(self, rho, op, dt):
        rho_old = rho

        for stage in range(self.stages):
            rho = rho_old + 0.5*dt*(op(rho)+op(rho_old))

        return rho

