### You are in charge of the cake for your niece's birthday and have decided
### the cake will have one candle for each year of her total age. 
### When she blows out the candles, she’ll only be able to blow out the tallest ones. 
### Your task is to find out how many candles she can successfully blow out. 

### For example, if your niece is turning years old, and the cake will have candles 
### of height 4,4 ,3 , 1 she will be able to blow out 2 candles successfully, 
### since the tallest candles are of height 4 and there are 2 such candles. 

### Sample Input:

### 4
### 3 2 1 3

### Sample Output:
### 2


import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.

def birthdayCakeCandles(ar):
    mx = max(ar)
    i = 0
    j = 0
    for i in ar:
        if i == mx:
            j+=1
            i+=1
    return (j)        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

