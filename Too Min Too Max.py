def x():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    c = 0
    b = a[-1]
    for x in [0, -2, 1, -1]:
        c += abs(b - a[x])
        b = a[x]
    return str(c)
        
t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))