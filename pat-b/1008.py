#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

n, w = map(int, input().split())
list = [i for i in input().split()]

if w == 0:
    res = list
else:
    while w > n:
        w = w - n

    res = list[-w:] + list[:n - w]
print(' '.join(res))