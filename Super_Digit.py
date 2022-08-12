#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    sm = 0    
    for i in n:
        sm += int(i)
    def super_digit(a): 
        def sum_digit(a):
            if a // 10 < 10:
                return a%10 + a//10
            else:
                return a%10 + sum_digit(a//10)
        if a < 10:
            return a
        else:
            return super_digit(sum_digit(a))
    return super_digit(k*super_digit(sm))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
