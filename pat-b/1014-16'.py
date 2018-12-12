#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''


s1 = input()
s2 = input()
s3 = input()
s4 = input()

day_dic = {'A': 'MON', 'B': 'TUE', 'C': 'WED',
           'D': 'THU', 'E': 'FRI', 'F': 'SAT',
           'G': 'SUN'}

leng12 = min(len(s1), len(s2))
leng34 = min(len(s3), len(s4))

iter = 0
for i in range(leng12):
    if s1[i].isupper() and s1[i]==s2[i]:
        d1 = day_dic[s1[i]]
        for j in range(i+1, leng12):
            if s1[j] == s2[j]:
                if s1[j].isdigit():
                    d2 = int(s1[j])
                    break
                elif s1[j].isupper():
                    d2 = ord(s1[j]) -55
                    break
        break

for i in range(leng34):
    if s3[i] == s4[i] and s3[i].isalpha():
        d3 = i
        break

print("{} {:0>2d}:{:0>2d}".format(d1, d2, d3))


