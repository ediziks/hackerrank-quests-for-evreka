#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, arr):
    pair = 0
    for i in arr[::-1]:
        if arr.count(i) >= 1 and i != 0:
            pair += arr.count(i) // 2 
        if i != 0:
            n += 1
        for j in arr[::-1]:
            if j == i:
                ar.remove(j)
    
    return pair

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
