#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    ls = [s[i] for i in range(len(s))]

    valley, level = 0, 0

    for step in ls:
        if step == 'U':
            level += 1
            if level == 0:
                valley += 1
        else:
            level -= 1        

    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
