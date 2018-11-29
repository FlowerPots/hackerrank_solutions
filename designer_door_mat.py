'''Mr. Vincent works in a door mat manufacturing company. One day, he
designed a new door mat with the following specifications:

Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)

The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

Sample Designs
    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

Input Format
A single line containing the space separated values of  and .

Constraints
5 < N < 101
15 < M < 303

Output Format
Output the design pattern.
'''

N, M = [int(x) for x in input().split()]

before_middle = int(N/2)

'''Make list of indexes for each row
for further computations of quantities of chars in the row.
'''
_pattern = \
    [i for i in range(1, before_middle+1, 1)] + \
    [0] + \
    [i for i in range(before_middle, 0, -1)]

''' Use the following format string.
'{message:{fill}{align}{width}}'.format(variables)'.
'''
[print('{heart:{fill}{align}{width}}'.format(
    heart = '.|.' * ((i*2)-1),
    fill = '-',
    align = '^',
    width = M,
    )) if i != 0 else print('{:-^{}}'.format('WELCOME', M))
    for i in _pattern]
