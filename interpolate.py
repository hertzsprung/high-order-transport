class Upwind:
    def __call__(self, rho, i):
        return rho[i-1]

class Linear:
    def __call__(self, rho, i):
        l = rho[i-1]
        r = rho[i]

        Cf = rho.mesh.faceCentre(i)

        distance_l = Cf - rho.mesh.cellCentre(i-1)
        distance_r = rho.mesh.cellCentre(i) - Cf

        if distance_l < 0:
            distance_l += 1

        if distance_r < 0:
            distance_r += 1

        distance_total = distance_l + distance_r

        weight_l = (distance_total - distance_l)/distance_total
        weight_r = (distance_total - distance_r)/distance_total

        return weight_l*l + weight_r*r

class HighOrder:
    def __init__(self, order, mesh, stencil):
        pass

    def __call__(self, rho, i):
        return rho[i-1]

