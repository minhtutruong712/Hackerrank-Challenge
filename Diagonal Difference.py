import math
import os
import random
import re
import sys


"""
Function description

Complete the DiagonalDifference function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers

Return

int: the absolute diagonal difference
"""

def diagonalDifference(arr):
    prim_diag = 0 
    sec_diag = 0    
    for i in range(0,n):
        prim_diag += arr[i][i]    
        sec_diag += arr[i][n-i-1]
    return abs(prim_diag-sec_diag)    

if __name__ == '__main__':
    """n is the number of rows (the number of columns)"""
    print('Please enter n')
    n = int(input().strip())

    arr = []
    print ('Please enter array element')
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
