N = int(input())

win1, win2 = 0, 0


def judgeFunc(s1, s2, s3, s4):
    if s2 == s4:
        return 0
    elif s2 == s1 + s3:
        return 1
    elif s4 == s1 + s3:
        return -1
    else:
        return 0

for i in range(N):
    s1, s2, s3, s4 = [int(i) for i in input().split()]
    if judgeFunc(s1, s2, s3, s4)>0:
        win1 += 1
    elif judgeFunc(s1, s2, s3, s4)<0:
        win2 += 1

print("{} {}".format(win2, win1))