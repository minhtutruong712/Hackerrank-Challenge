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
        sm += int(i)                            # sum the digits in the string first to avoid time runout
    def super_digit(a):             
        def sum_digit(a):
            if a // 10 < 10:                    # base condition is integer with 2 digits
                return a%10 + a//10             
            else:
                return a%10 + sum_digit(a//10)  # recur until meet the base condition
        if a < 10:                      
            return a
        else:
            return super_digit(sum_digit(a))    # if a is not 1 digit integer call the function sum_digit    
    return super_digit(k*super_digit(sm))       # return the super digit if multiply the string by k times    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
