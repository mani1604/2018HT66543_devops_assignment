#!/usr/local/bin/python3.7

# =========================================================================================
#
# NAME:           array_sum.py
# DESCRIPTION:    Python module to find out the sum of all elements of a list
# AUTHOR:         Manish Sharma
# VERSION:        1.0
# CREATED:        Oct 16, 2019
#
# =========================================================================================

import sys

def simpleArraySum(n, ar):
    t = 0
    for i in range(0,n):
        t += ar[i]
        
    return t

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
