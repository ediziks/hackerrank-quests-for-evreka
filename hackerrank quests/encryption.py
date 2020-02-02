#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s = s.replace(' ', '')

    sqr = math.sqrt(len(s))

    row = int(sqr)

    if row >= sqr:
        col = row
    else:
        col = row + 1

    a = ''
    for i in range(0, col):
        for j in range(i, len(s), col):
            a += (s[j])
        a += ' '
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
