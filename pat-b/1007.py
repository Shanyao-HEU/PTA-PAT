#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

from math import sqrt

def is_prime(n, primes):
    up_data = int(sqrt(n))
    for prime in primes:
        if prime > up_data:
            break
        if n % prime == 0:
            return False
    return True

n = int(input())
last_prime, next_prime = 2, 3
count = 0
primes = [2, 3]
if n > 4:
    for number in range(5, n+1):
        if is_prime(number, primes):
            primes.append(number)
            last_prime = next_prime
            next_prime = number
            if next_prime - last_prime == 2:
                count += 1 

print(count)


