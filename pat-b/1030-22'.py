#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

n, p = [int(i) for i in input().split()]

b = [int(c) for c in input().split()]
b.sort()

m = 0
for i in range(n):
    for j in range(i+m, n):
        if b[j]*p<b[j]:
            break
        m+=1

print(m)


