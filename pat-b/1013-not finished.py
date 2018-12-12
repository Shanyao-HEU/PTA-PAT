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
def print_primes(n_list):
    res = ''
    row = len(n_list) // 10
    print(row)
    if row == 0:
        for r in row:
            res = res + str(r) + ' '
            print(res[:-1])
    else:
        for r in range(row):
            res = ''
            for num in n_list[10*r:10*r+9]:
                res = res + str(num) + ' '
            print(res[:-1])
        res = ''
        for r in n_list[10*row:]:
            res = res + str(r) + ' '
        print(res[:-1])

def find_primes(m, n):
    i = 2
    res = []
    m1 = m
    while 1:
        if is_prime(i):
            m1 -= 1
            i += 1
            if m1 == 1:
                break
        else:
            i += 1

    while 1:
        if is_prime(i):
            res.append(i)
            i += 1
            if len(res) == n-m+1:
                break
        else:
            i += 1

    return res

m, n = [int(i) for i in input().split()]
print_primes(find_primes(m, n))