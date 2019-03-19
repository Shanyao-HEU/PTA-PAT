N = int(input())

num_score = {}

for i in range(N):
    n, s = input().split()
    n1, n2 = [int(c) for c in n.split('-')]
    num_score.setdefault(n1, 0)
    num_score[n1] += int(s)

sort_dic = sorted(num_score.items(), key=lambda x: x[1], reverse=True)
print("{} {}".format(sort_dic[0][0], sort_dic[0][1]))