def func(n):
    return n//2 + n//3 + n//5
    
n = int(input())

print(len(set([func(i) for i in range(n+1)])))