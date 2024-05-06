def x():
    n = int(input())
    a = [*map(int, input().split())]
    a.sort()
    c = float("inf")
    for i in range(1,n-1):
        r = abs(a[i] - a[i-1]) + abs(a[i] - a[i+1])
        if r < c:
            c = r
    return str(c)    

t = int(input())
a =[]
for _ in range(t):
    a.append(x())
print("\n".join(a)) 