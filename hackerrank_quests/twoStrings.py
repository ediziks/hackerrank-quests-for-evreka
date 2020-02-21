#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    for i in range(q):
        res = 'YES'
        cnt = 0
        for j in s1:
            if j not in s2:
                cnt += 1
        if cnt == len(s1):
            res = 'NO'
            return res
        else:
            return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + "\n")

    fptr.close()
