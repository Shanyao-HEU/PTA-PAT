#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

a, b = [int(i) for i in input().split()]
q = a // b
r = a - b*q
print(q, r)