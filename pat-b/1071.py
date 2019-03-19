T, K = [int(i) for i in input().split()]

def func(n1, b, t, n2, now):
    if t > now:
        print('Not enough tokens.  Total = {}.'.format(now))
    else:
        if b ==1 and n2 > n1:
            now += t
            print('Win {}!  Total = {}.'.format(t, now))
        elif b == 0 and n2 < n1:
            now += t
            print('Win {}!  Total = {}.'.format(t, now))
        else:
            now -= t
            print('Lose {}.  Total = {}.'.format(t, now))
    
    return now
          
    

for i in range(K):
    n1, b, t, n2 = [int(c) for c in input().split()]
    T = func(n1, b, t, n2, T)
    if T <= 0:
        print('Game Over.')
        break
        
    