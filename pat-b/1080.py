p, m, n = map(int, input().split())
scores = {}
for i in range(p):
    stu, gp = input().split()
    if stu not in scores:
        scores[stu] = [int(gp), -1, -1]
    else:
        scores[stu][0] = int(gp)

for i in range(m):
    stu, gm = input().split()
    if stu not in scores:
        scores[stu] = [-1, int(gm), -1]
    else:
        scores[stu][1] = int(gm)

for i in range(n):
    stu, gf = input().split()
    if stu not in scores:
        scores[stu] = [-1, -1, int(gf)]
    else:
        scores[stu][2] = int(gf)
        
passed = {}

for stu, score in scores.items():

    if score[1] > score[2]:
        gfinal = int(round((score[1]*0.4+score[2]*0.6)))
    else:
        gfinal = score[2]
    if score[0]>= 200 and gfinal >= 60:
        passed[stu] = [score[0], score[1], score[2], gfinal]
        
sorted_passed = sorted(passed.items(), key=lambda x: (x[1][-1], -ord(x[0][0])), reverse=True)

for k, v in sorted_passed:
    print(k, v[0], v[1], v[2], v[3])
    