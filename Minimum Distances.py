#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(n,l):
    # Write your code here
    d=n
    for i in range(n-1):
        if l[i] in l[i+1:]:
            k=l.index(l[i],i+1)
            if k-i<d:
                d=k-i
    if d==n:
        return -1
    else:
        return d

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(n,a)

    fptr.write(str(result) + '\n')

    fptr.close()
