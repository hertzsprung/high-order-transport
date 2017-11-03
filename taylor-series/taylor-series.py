#!/usr/bin/python3
import numpy as np

# cubicFit matrix
A = [
    [1, -5/2, (-5/2)**2, (-5/2)**3],
    [1, -3/2, (-3/2)**2, (-3/2)**3],
    [1, -1/2, (-1/2)**2, (-1/2)**3],
    [1,  1/2, ( 1/2)**2, ( 1/2)**3]
]

print(np.linalg.inv(A))
print()

# Taylor series expansion for 4-point upwind-biased stencil
# for face approximation (a la cubicFit)
A = [
    [1, -5/2, 25/8, -125/48],
    [1, -3/2, 9/8, -27/48],
    [1, -1/2, 1/8, -1/48],
    [1, 1/2, 1/8, 1/48]
]

print(np.linalg.inv(A))
print()

# Taylor series coefficients for 5-point upwind-biased stencil
# for gradient calculation
A = [
    [1, -5/2, 5**2/8, -5**3/48, -5**4/384],
    [1, -3/2, 3**2/8, -3**3/48, -3**4/384],
    [1, -1/2,    1/8,    -1/48, 1/384],
    [1,  1/2,    1/8,     1/48, 1/384],
    [1,  3/2, 3**2/8,  3**3/48, 3**4/384]
]

print(np.linalg.inv(A))
print()

A = [
    [-2 - -3, 1/2*((-2)**2 - (-3)**2), 1/3*((-2)**3 - (-3)**3), 1/4*((-2)**4 - (-3)**4)],
    [-1 - -2, 1/2*((-1)**2 - (-2)**2), 1/3*((-1)**3 - (-2)**3), 1/4*((-1)**4 - (-2)**4)],
    [ 0 - -1, 1/2*(  0 **2 - (-1)**2), 1/3*(  0 **3 - (-1)**3), 1/4*(  0 **4 - (-1)**4)],
    [ 1 -  0, 1/2*(  1 **2 -   0 **2), 1/3*(  1 **3 -   0 **3), 1/4*(  1 **4 -   0 **4)]
]

print(np.array(A))
print(np.linalg.inv(A))
