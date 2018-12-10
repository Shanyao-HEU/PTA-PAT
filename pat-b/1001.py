n = int(input())
iter = 0

while int(n) != 1:

    if n % 2 == 0:
        n = n/2
        iter += 1
    else:
        n = (3*n+1) / 2
        iter += 1

print(iter)

