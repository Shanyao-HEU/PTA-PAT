N, M = [int(i) for i in input().split()]
nums = [i for i in input().split()]

def func(name, things, nums):
    res = ''
    res_num = 0
    for t in things:
        if t in nums:
            res_num += 1
            res = res +t +' '
            
    
    if res_num:
        flag = 1
        print('{}: {}'.format(name, res[:-1]))
    else:
        flag = 0
        
    return flag, res_num

res = 0
res_things = 0
for i in range(N):
    temp = [t for t in input().split()]
    flag, res_num = func(temp[0], temp[2:], nums)
    res += flag
    res_things += res_num

print(res, res_things)
    