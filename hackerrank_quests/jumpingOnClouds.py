#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    step = 0
    i = 0
    while i < len(c):
        try:
            if c[i+2] == 0:
                step += 1
                i += 2
            elif c[i+1] == 1:
                step += 1
                i += 2
            elif c[i+2] == 1:
                step += 2
                i += 3
            elif c[i+3] == 1:
                step += 2
                i += 4
        except:
            break
    
    if i+1 != len(c):
        step += 1
    
    return step

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
