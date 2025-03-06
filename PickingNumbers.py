#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    longest_subarray_length=0

    for i in a:
        subarray_length=0
        for j in a:
            if i==j or j==i+1:
                subarray_length+=1
        longest_subarray_length=max(longest_subarray_length,subarray_length)
    return longest_subarray_length
                 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
