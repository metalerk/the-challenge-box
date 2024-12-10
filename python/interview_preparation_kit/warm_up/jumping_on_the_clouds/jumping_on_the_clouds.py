#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    current_step = 0
    clouds = len(c)
    steps = 0
    
    for step in c:
        if (current_step + 2) <= (clouds - 1) and not c[current_step + 2]:
            steps += 1
            current_step += 2
        elif (current_step + 1) <= (clouds - 1) and not c[current_step + 1]:
            steps += 1
            current_step += 1
    return steps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()