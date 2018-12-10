#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''
n = int(input())
b = n//100
s = (n-b*100)//10
g = n - b*100 -s*10

res = ''
res = b*'B'+s*'S'
for i in range(1, g+1):
    res += str(i)

print(res)