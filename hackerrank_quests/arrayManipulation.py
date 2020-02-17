#!/bin/python

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0]*(n+2)
    for a, b, k in queries:
        arr[a]+=k
        arr[b+1]-=k
    result = acc = 0
    for x in arr:
        acc+=x
        result = max(result, acc)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in xrange(m):
        queries.append(map(int, raw_input().rstrip().split()))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
