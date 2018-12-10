#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

n = int(input())


i = 0

for num in range(2, n-1):
    if is_prime(num) and is_prime(num+2):
        i += 1

print(i)


