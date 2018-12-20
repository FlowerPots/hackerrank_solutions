#!/usr/bin/python3

from math import sqrt
from cmath import phase

cnum = complex(input().strip())

r = sqrt(cnum.real**2 + cnum.imag**2)
phi = phase(cnum)

print('{}\n{}'.format(r, phi))
