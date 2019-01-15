#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

N = int(input())
dic = {}
for i in range(N):
    n1, n2, n3 = [n for n in input().split()]
    dic[n2] = (n1, n3)

M = int(input())
m_lst = [i for i in input().split()]
for m in m_lst:
    print("{} {}".format(dic[m][0], dic[m][1]))
