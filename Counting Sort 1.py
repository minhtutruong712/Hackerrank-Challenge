import math 
import os
import random 
import re
import sys

"""
Challenge
Given a list of integers, count and return the number of times 
each value appears as an array of integers.

Function Description

Complete the countingSort function in the editor below.

countingSort has the following parameter(s):

arr[n]: an array of integers
Returns

int[100]: a frequency array

Explanation
Each of the resulting values  represents the number of times  appeared in .

"""
def countingSort(arr):
    freq = [0]
    freq = freq*100
    arr.sort()
    for i in range(len(freq)):
        freq[i] = arr.count(i) 
    return freq   

if __name__ == '__main__':

    print ('Please enter n')
    n = int(input().strip())

    print ('Please enter the array')
    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)
    print(result)


