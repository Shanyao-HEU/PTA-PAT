#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

n = input()
nums = set()
outer = set()
x = map(int, input().split())
for i in x:
    outer.add(i)
    while i != 1:
        if i in nums:
            if i in outer:
                outer.remove(i)
            break

        else:
            nums.add(i)

        if i % 2 == 0:
            i /= 2

        else:
            i = (i*3+1)/2

s = [i for i in outer]
res = ''
for o in s[::-1]:
    res = res + str(o) + ' '
print(res[:-1])