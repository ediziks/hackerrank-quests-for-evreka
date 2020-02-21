#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(mag, note):
    if Counter(note) - Counter(mag) == {}:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    mag = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(mag, note)
