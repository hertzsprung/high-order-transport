class Upwind:
    def __call__(self, rho, i, position):
        return rho[i-1]

class Linear:
    def __call__(self, rho, i, position):
        l = rho[i-1]
        r = rho[i]

        distance_l = position - rho.mesh.cellCentre(i-1)
        distance_r = rho.mesh.cellCentre(i) - position

        if distance_l < 0:
            distance_l += 1

        if distance_r < 0:
            distance_r += 1

        distance_total = distance_l + distance_r

        weight_l = (distance_total - distance_l)/distance_total
        weight_r = (distance_total - distance_r)/distance_total

        return weight_l*l + weight_r*r

