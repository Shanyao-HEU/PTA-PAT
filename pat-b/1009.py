#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

word = [i for i in input().split()]
res = ''
for w in word[::-1]:
    res = res + w + ' '
print(res[:-1])