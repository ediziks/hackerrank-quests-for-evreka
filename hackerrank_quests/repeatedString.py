#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    s = list(s)
    res = 0
    ocr = n // len(s)
    rst = n % len(s)

    res += ocr * s.count('a')

    for i in s[:rst]:
        if i == 'a':
            res += 1

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
