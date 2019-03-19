N, M = map(int, input().split())
scores = [int(i) for i in input().split()]
ansers = [i for i in input().split()]

for i in range(N):
    stu = [s for s in input().split()]
    sco = 0
    for j in range(M):
        if stu[j] == ansers[j]:
            sco += scores[j]
    print(sco)
