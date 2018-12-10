#!/usr/bin/env python
# encoding: utf-8

'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

n = str(input())
res = 0
pinyin = ''
dic = {'1': 'yi', '2': 'er', '3': 'san',
		'4': 'si', '5': 'wu', '6': 'liu',
		'7': 'qi', '8': 'ba', '9': 'jiu', '0': 'ling'}

for s in n:
    res += int(s)
for r in str(res):
    pinyin = pinyin + dic[r] + ' '
print(pinyin[:-1])

