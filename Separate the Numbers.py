#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    length=len(s)
    
    for i in range(1,length//2+1):
        num=seq=s[:i]
        while len(seq)<length:
            num=int(num)+1
            seq+=str(num)
        if seq==s:
            print("YES",s[:i])
            return
    print("NO")
        

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
