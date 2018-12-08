#!/bin/python3

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
