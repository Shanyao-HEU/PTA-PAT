#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

import re

hand = re.findall('[[](.*?)[]]', input())
eye = re.findall('[[](.*?)[]]', input())
mouth = re.findall('[[](.*?)[]]', input())

# print(hand, eye, mouth)

def smile(lst, hand, eye, mouth):
    res = ''

    try:
       temp1 = hand[lst[0]-1]
       temp2 = eye[lst[1]-1]
       temp3 = mouth[lst[2]-1]
       temp4 = eye[lst[3]-1]
       temp5 = hand[lst[4]-1]
       res = temp1+temp2+temp3+temp4+temp5
    except:
       return r'Are you kidding me? @\/@'
    return res


N = int(input())
for i in range(N):
    num_lst = [int(n) for n in input().split()]
    print(smile(num_lst, hand, eye, mouth))

