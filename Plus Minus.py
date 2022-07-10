import math
import os
import random
import re
import sys

"""
Function Description

Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):

int arr[n]: an array of integers
Print
Print the ratios of positive, negative and zero values in the array. 
Each value should be printed on a separate line with 6 digits after the decimal. 
The function should not return a value.

Sample Input

STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
Sample Output

0.500000
0.333333
0.166667

"""

def plusMinus(arr):
    count_neg = 0 
    count_pos = 0
    count_0 = 0
    for i in arr: 
        if i == 0: 
            count_0 +=1
        if i < 0:
            count_neg +=1
        if i > 0:
            count_pos +=1
    print ('{:.6f}'.format(round(count_pos/len(arr),6)))
    print('{:.6f}'.format(round(count_neg/len(arr),6)))
    print('{:.6f}'.format(round(count_0/len(arr),6)))            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)