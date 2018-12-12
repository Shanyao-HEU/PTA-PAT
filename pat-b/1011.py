#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

def func(i, a, b, c):
    if a + b > c:
        print("Case #{}: true".format(i+1))
    else:
        print("Case #{}: false".format(i+1))
    return

n = int(input())
for it in range(n):
    a, b, c = [int(num) for num in input().split()]
    func(it, a, b, c)
