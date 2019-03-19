n_lst = input()
p1 = input()
p2 = input()

def plusOn(a, b, c, on):
    if on != 0:
        flag = (a+b+c) // on
        left = (a+b+c) % on
    else:
        flag = (a+b+c) // 10
        left = (a+b+c) % 10       
    return flag, left

result = ''

flag_temp = 0

for i in range(max(len(p1), len(p2))):
    try:
        a = int(p1[::-1][i])
    except:
        a = 0
    try:
        b = int(p2[::-1][i])
    except:
        b = 0
    flag, left = plusOn(a, b, flag_temp, int(n_lst[::-1][i]))
    
    result += str(left)
    
    flag_temp = flag

print(int(result[::-1]))
    
    
