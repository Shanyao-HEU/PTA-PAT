#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

from datetime import datetime

n = int(input())

today = datetime.strptime("2014/09/06", "%Y/%m/%d")
name_age = {}
for i in range(n):
    name, date = [c for c in input().split()]
    date = datetime.strptime(date, "%Y/%m/%d")
    age = today - date
    if age.days <= 73049 and age.days >= 0:
        name_age[name] = age.days

sorted_age = sorted(name_age.items(), key=lambda x: x[1])
print(len(sorted_age), sorted_age[-1][0], sorted_age[0][0])