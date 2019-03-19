n = int(input())

scores = {}

def shot(temp):
    return 1/(int(temp[1])** 2 + int(temp[2]) ** 2)
for i in range(n):
        temp = [t for t in input().split()]
        scores[temp[0]] = shot(temp)

sort_scores = sorted(scores.items(), key=lambda x: x[1])
print("{} {}".format(sort_scores[-1][0], sort_scores[0][0]))