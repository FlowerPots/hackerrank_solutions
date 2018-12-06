'''Polar coordinates are an alternative way of representing Cartesian 
coordinates or Complex Numbers z.

z = x + yj

A complex number   Capture.PNG is completely determined by its real part x and
imaginary part y.
Here, j is the imaginary unit.

A polar coordinate (r, phi) is completely determined by modulus r and phase 
angle phi.

If we convert complex number z to its polar coordinate, we find:
r: Distance from z to origin, i.e. squar root from (x^2+y^2), 
phi: Counter clockwise angle measured from the positive x-axis to the line 
segment that joins  to the origin.

Python's cmath module provides access to the mathematical functions for 
complex numbers.

cmath.phase
This tool returns the phase of complex number z (also known as the argument 
of z).
>>> phase(complex(-1.0, 0.0))
3.1415926535897931

abs
This tool returns the modulus (absolute value) of complex number .
>>> abs(complex(-1.0, 0.0))
1.0

Task 
You are given a complex z. Your task is to convert it to polar coordinates.

Input Format
A single line containing the complex number z. Note: complex() function can 
be used in python to convert the input as a complex number.

Constraints
Given number is a valid complex number.

Output Format
Output two lines: 
The first line should contain the value of r.
The second line should contain the value of phi.
'''

from math import sqrt
from cmath import phase

cnum = complex(input().strip())

r = sqrt(cnum.real**2 + cnum.imag**2)
phi = phase(cnum)

print('{}\n{}'.format(r, phi))
