#!/usr/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations


def biggerIsGreater(w):

    word = list(w)

    def _find_pivot(w):
        try:
            for i in range(len(w)-1, 0, -1):
                if w[i-1] < w[i]:
                    pivot = i - 1
                    break
            return True, pivot

        except:
            return None, 0

    def _substitute(w, pivot):
        suffix = w[pivot+1:]

        if len(set(suffix)) > 1:
            if_bigger = tuple(char for char in suffix if char > w[pivot])

            sub = min(if_bigger, key=str)

            _index = w.rfind(sub)

        else:
            _index = pivot+1
        '''Index of substitution for pivot.
        '''
        return _index

    def _replace(w, pivot, sub):
        w = list(w)

        w[pivot], w[sub] = w[sub], w[pivot]

        return tuple(w)

    def _reverse(new_word, pivot):
        suffix = list(new_word[pivot+1:])

        if len(set(suffix)) == 2:
            ''' When all chars to the right
            after pivot is the same.'''
            suffix.sort()
        else:
            suffix.reverse()

        prefix = list(new_word[:pivot+1])
        reversed_word = prefix + suffix

        return tuple(reversed_word)

    def _output(w):
        return ''.join(str(i) for i in w)

    ok, pivot = _find_pivot(w)  # Just an index integer.

    if ok:

        sub = _substitute(w, pivot)

        new_word = _replace(w, pivot, sub)

        reversed_word = _reverse(new_word, pivot)

        return _output(reversed_word)

    else:
        return 'no answer'


if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
