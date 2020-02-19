#!/bin/python3

import os
import sys
import heapq as h

#
# Complete the cookies function below.
#
def cookies(k, A):
    # Write your code here.
    h.heapify(A)
    opr = 0

    while A[0] < k and len(A) > 1:
        h.heappush(A, h.heappop(A) + 2 * h.heappop(A))
        opr += 1
    
    return opr if A[0] >= k else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
