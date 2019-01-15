#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

N = int(input())
scores = [int(i) for i in input().split()]
k_scores = [int(i) for i in input().split()]

res = ''
for k in k_scores[1:]:
    res = res + str(scores.count(k)) + ' '
print(res[:-1])