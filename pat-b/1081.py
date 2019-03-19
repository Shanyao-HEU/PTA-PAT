n = int(input())

def output(s):
    shuzi, zimu = [], []
    flag = 1
    if len(s) < 6:
        print("Your password is tai duan le.")
    else:
        for i in s:
            if i == '.':
                continue
            elif i.isdigit():
                shuzi.append(i)
            elif i.isalpha():
                zimu.append(i)
            else:
                flag = 0
                break
        if flag:
            if shuzi and zimu:
                print("Your password is wan mei.")
            elif shuzi:
                print("Your password needs zi mu.")
            else:
                print("Your password needs shu zi.")
        else:
            print("Your password is tai luan le.")
                
for i in range(n):
    output(input())
    