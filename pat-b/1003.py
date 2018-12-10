#!/usr/bin/env python
# encoding: utf-8

'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''
import re

n = int(input())

for i in range(n):
    input_str = input()

    pa = re.compile(r'(?P<a>A*)P(?P<b>A+)T(?P<c>A*)')

    if pa.match(input_str):
        co = re.split(r'P|T', input_str)
        if len(co[0]) * len(co[1]) == len(co[2]):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')