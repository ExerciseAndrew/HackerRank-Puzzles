
### Write a function that takes in an array and outputs 
### the minimum or maximum sum (the array's sum minus its maximum
### and minimum elements)
### ex: input: [1, 2, 3, 4, 5,]
###     output: [10 14]

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    print (sum(arr)-max(arr), sum(arr)-min(arr))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
