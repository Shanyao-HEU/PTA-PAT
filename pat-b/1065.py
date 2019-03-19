N = int(input())
coup = []
for i in range(N):
    a, b = input().split()
    coup.append(a)
    coup.append(b)

input()
persons = [i for i in input().split()]

danshen = []
for person in persons:
    if person not in coup:
        danshen.append(person)
        
danshen.sort()
print(len(danshen))
print(" ".join([str(i) for i in danshen]))

    
        
    