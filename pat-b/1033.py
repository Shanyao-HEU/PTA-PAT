#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

s1 = input()
s2 = input()

res = ''



for i in s2:
    if i.isalpha():
        if i.upper() not in s1:
            if '+' in s1:
                if not i.isupper():
                    res += i
            else: res += i
    else:
        if not i in s1:
            res += i

print(res)
