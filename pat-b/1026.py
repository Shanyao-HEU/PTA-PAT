#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

C1, C2 = [int(i) for i in input().split()]
CLK_TCK = 100
s = round((C2-C1)*1.0/CLK_TCK)
res_h = int(s/3600)
res_m = int(s%3600/60)
res_s = int(s) - res_h*3600 - res_m*60
print("{:0>2d}:{:0>2d}:{:0>2d}".format(res_h, res_m, res_s))
