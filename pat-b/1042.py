#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

s = input()
s_alpha = [i.lower() for i in s if i.isalpha()]
s_set = set(s_alpha)

dic = {}
for k in s_set:
    dic[k] = s_alpha.count(k)

def func(a):
    return a[1], -ord(a[0])


sort_dic = sorted(dic.items(), key=func, reverse=True)
print("{} {}".format(sort_dic[0][0], sort_dic[0][1]))