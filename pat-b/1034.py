#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

def preprocess(s):

    return s

def process_result(s):

    return s

def compute(s):
    return s

def main():
    s1, s2 = [i for i in input().split()]
    r1, r2 = compute(s1), compute(s2)
    s1, s2 = preprocess(s1), preprocess(s2)

    print("{} + {} = {}".format())
    print("{} - {} = {}".format())
    print("{} * {} = {}".format())
    print("{} / {} = {}".format())
