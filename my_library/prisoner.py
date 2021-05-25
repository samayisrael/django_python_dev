import math
import os
import random
import re
import sys

# Save the Prisoner!!
# n  is prisoners
# m is candies
# s is starting chair

def saveThePrisoner(n, m, s):
    # if the amount of candies is one, than we just need to warn the starting person.
    if m == 1:
        return s

    res = s + m - 1
    res %= n
    if res == 0:
        return n
    else:
        return res

#print(saveThePrisoner(7,19,2)) # wrrks
#print(saveThePrisoner(208526924,756265725,150817879))
#print(saveThePrisoner(15,37,14))


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    fptr = open('C:\\Users\\samay\\intense-dusk-10038\\my_library\\output.txt', 'w')
    inputptr = open('C:\\Users\\samay\\intense-dusk-10038\\my_library\\input.txt', 'r')

    t = int(inputptr.readline())

    for t_itr in range(t):

        nms = inputptr.readline().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
