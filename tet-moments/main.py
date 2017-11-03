#!/usr/bin/env python3
from tetrahedron import Tetrahedron
from triangle import Triangle

if __name__ == '__main__':
    t = Tetrahedron(
        [2, 3, 1],
        [1, 1, 4],
        [4, 4, 2])
    print(t)

    print('volume', t.volume())
    print('zeroth moment', t.moment(0, 0, 0))
    print('(0 2 0)th moment', t.moment(0, 2, 0))

    t = Triangle(
        [2, 3, 1],
        [1, 1, 4],
        [4, 4, 2])

    print(t)
    print('area', t.area())
    print('zeroth moment', t.moment(0, 0, 0))
