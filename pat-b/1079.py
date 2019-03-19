num = input()
step = 0

def is_palin(number):
    n = str(number)
    m = n[::-1]
    return m == n
    
while step < 10:
    num_rev = num[::-1]
    temp = str(int(num)+int(num_rev))
    print("{} + {} = {}".format(num, num_rev, temp))
    if is_palin(temp):
        print("{} is a palindromic number.".format(temp))
        break
    else:
        num = temp
    step += 1

if step >= 10:
    print("Not found in 10 iterations.")