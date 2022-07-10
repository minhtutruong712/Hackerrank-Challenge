#!/bin/python3

import math
import os
import random
import re
import sys

"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.

"""

def miniMaxSum(arr):
    arr.sort()
    sum_min = 0 
    sum_max = 0
    for i in range(0,4):
        sum_min += arr[i]
    for i in range(len(arr)-4, len(arr)):
        sum_max += arr[i]
    print (sum_min, sum_max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)