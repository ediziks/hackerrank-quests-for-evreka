#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countTriplets function below.
def countTriplets(arr, r):
    count = 0
    d, pairs = {}, {}

    for i in reversed(arr):
        if i*r in pairs:
                count += pairs[i*r]
        if i*r in d:
                pairs[i] = pairs.get(i, 0) + d[i*r]

        d[i] = d.get(i, 0) + 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
