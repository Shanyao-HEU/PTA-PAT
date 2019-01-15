#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''
import math

n, sym = [i for i in input().split()]

x = int(math.sqrt((int(n)+1)/2))

for i in range(-x+1, x):
    if i < 0:
        i = -i
        num_sym = 2*i + 1
        num_space = (2*x - 1 - num_sym)//2
        print(num_space * ' ' + num_sym*sym + num_space*' ')
    elif i == 0:
        num_sym = 1
        num_space = (2 * x - 1 - num_sym) // 2
        print(num_space * ' ' + num_sym * sym + num_space * ' ')
    else:
        num_sym = 2 * i + 1
        num_space = (2 * x - 1 - num_sym) // 2
        print(num_space * ' ' + num_sym * sym + num_space * ' ')
print(int(n)-2*x**2+1)