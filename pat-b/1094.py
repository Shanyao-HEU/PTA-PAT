import math

def isPrime(n):
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
    
l, k = map(int, input().split())
nums = input()
def search(nums, l, k):
    for i in range(l-k):
        if isPrime(int(nums[i:i+k])):
            return int(nums[i:i+k])
       
    return  '404'
    
print(search(nums, l, k))