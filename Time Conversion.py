
import math
import os
import random
import re
import sys

"""
Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in 12 hour format
Returns

string: the time in 24 hour format
"""

def timeConversion(s):
    # Write your code here    
    if s[:2] == '12' and  s[-2:] == 'AM':
        s = s.replace('12','00')
    if s[-2:] == 'PM':
        if s[:2] == '12': 
            s = s.replace('PM','')
        else:
            s1 = int(s[:2])+12                
            s = s.replace(s[:2],str(s1))
    s = s.replace('AM','')
    s = s.replace('PM','')
    return s

    
if __name__ == '__main__':
    s = input()

    result = timeConversion(s)
    
    print(result)
