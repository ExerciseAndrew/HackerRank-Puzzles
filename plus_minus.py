### Print the ratioss of positive, negative, and "zero" values in a given array. 
### Each value should be printed on a separate line with 6 digits after the decimal
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):

    pos = sum(x > 0 for x in arr) / len(arr)
    neg = sum(x < 0 for x in arr) / len(arr)
    zer = sum( x == 0 for x in arr) / len(arr)

    print (format(pos, ".6f"))
    print (format(neg, ".6f"))
    print (format(zer, ".6f"))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
