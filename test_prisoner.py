#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    if m == 1:
        return s

    if m > n:
    # if there are more candies than prisoners, just use the modulous/remainder
        candies = m % n
    else:
    # otherwise, use the number
        candies = m

    return (s + candies) - 1

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    mydata_file = open('myinput.txt', 'r')
    #t = int(input())
    t = 100
    #mycurrentline = mydata_file.readline()
    #print(mycurrentline.split())

    for t_itr in range(t):
        #nms = input().split()
        #nms = [499999999,999999997,2]
        mycurrentline = mydata_file.readline()
        nms =  mycurrentline.split()
        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        print(result)
        #fptr.write(str(result) + '\n')

    #fptr.close()
