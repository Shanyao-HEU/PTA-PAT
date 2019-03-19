#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

n = input()

temp = input().split()
num = [int(i) for i in temp]
rst = [int(i) for i in temp]

numlist = []
fin = []
for i in range(len(num)):
    while num[i] != 1:
        if num[i] % 2==0:
            num[i] = num[i] / 2
            numlist.append(num[i])
            
        else:
            num[i] = (num[i] * 3 + 1)/2
            numlist.append(num[i])
            
for x in range(len(rst)):
    if rst[x] not in numlist:
        fin.append(rst[x])
        
fin.sort(reverse=True)
a = []
for f in fin:
    a.append(str(int(f)))
    
print(' '.join(a))