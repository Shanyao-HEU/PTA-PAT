m, n, a, b, r = map(int, input().split())

def rep(points, a, b, r):
    points = [r if (point <= b and point >= a) else point for point in points]
    points = [str(point).zfill(3) for point in points]
    print(" ".join(points))
    
for i in range(m):
    temp = [int(t) for t in input().split()]
    rep(temp, a, b, r)
    
    