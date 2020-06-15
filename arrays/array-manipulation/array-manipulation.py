import math
import os
import random
import re
import sys

INIT = 0
END = 1
VALUE = 2

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    #add_list = queries.sort(key=lambda x: x[INIT], reverse=False)
    add_list = sorted(queries, key=lambda x: x[INIT], reverse=False)
    remove_list = sorted(queries, key=lambda x: x[END], reverse=False)
    complete_list = [ (key, add) for [key, _, add] in add_list]
    complete_list += [ (key, -remove) for [_, key, remove] in remove_list]
    complete_list = sorted(complete_list, key=lambda x: x[INIT], reverse=False)
    biggest = 0
    current = 0
    for i in complete_list:
        current += i[1] 
        if current > biggest:
            biggest = current
    return biggest
    
# [ 1, 2,  3,  4,  5,  6,  7,  8]
# [ 1, 1,  1,  1,  1,  1,  1,  1]
# [ 1, 9,  9,  9,  9,  9,  1,  1]
# [ 1, 9, 16, 16, 16,  9,  1,  1]
# [ 1, 9, 16, 16, 31, 24, 16, 16]
#

if __name__ == '__main__':
    f = open('instance7', 'r')

    nm = f.readline().split()
    n = int(nm[0])
    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append([int(x) for x in f.readline().rstrip().split()])

    result = arrayManipulation(n, queries)
    print(str(result) + '\n')

    f.close()

