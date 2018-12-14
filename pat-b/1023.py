#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

n_lst = [int(i) for i in input().split()]
num_lst = ''
for i in range(10):
    num_lst += n_lst[i]*str(i)
num_lst = list(num_lst)
num_lst.sort()

for i in range(len(num_lst)):
    if num_lst[i] == '0':
        continue
    else:
        res = num_lst[i]
        del num_lst[i]
        break

for i in num_lst:
    res += str(i)

print(res)
