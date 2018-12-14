#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

n = input()

freq = {}
for i in (n):
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1

sort_freq = sorted(freq.items(), key=lambda x: int(x[0]))

for k, v in sort_freq:
    print("{}:{}".format(k, v))
