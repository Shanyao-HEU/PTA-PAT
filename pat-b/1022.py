#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

a, b, d = [int(i) for i in input().split()]

temp = a + b
l = []
while True:
    temp, remainder = divmod(temp, d)
    l.append(str(remainder))
    if temp == 0:
        print("".join(l[::-1]))
        break