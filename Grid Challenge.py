#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#
# grid = ['abd', 'rtf', 'tyu']
def gridChallenge(grid):
    n = len(grid[0])                        # Count the number of elements in grid
    new_grid = []                           
    for e in grid: 
        new_grid.append("".join(sorted(e))) # Create new grid whose each element is sorted
    for i in range(n):                      # n is the len of each element in the grid    
        a = []                              # Store elements in 1 column - correspondingly with each loop
        for e in new_grid: 
            a.append(e[i])
        b = a.copy()                        # Create a new list then sort to compare with the old list
        b.sort()                            
        if b != a:                          # if 1 column that is not sorted return No immediately
            return 'NO'                         
    return 'YES'
       
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
