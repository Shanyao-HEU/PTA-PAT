#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

N = int(input())
num_lst = [n for n in input().split()]

nums = 0
num_sum = 0

for num in num_lst:
    try:
        num_ = float(num)
        if num_ >= -1000 and num_ <= 1000:
            if '.' in num:
                if len(num.split('.')[1]) < 3:
                    num_sum += num_
                    nums += 1
                else:
                    print("ERROR: {} is not a legal number".format(num))
            else:
                num_sum += num_
                nums += 1
        else:
            print("ERROR: {} is not a legal number".format(num))
    except:
        print("ERROR: {} is not a legal number".format(num))

if nums == 0:
    res = 'Undefined'
else:
    res = round(num_sum/nums, 2)
print("The average of {} numbers is {}".format(nums, res))
