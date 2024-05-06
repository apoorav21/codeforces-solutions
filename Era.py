def x():
    n = int(input())
    a = [*map(int, input().split())]
    p = 0
    for i in range(1, n+1):
        if a[i-1] > i+p:
            p += a[i-1] - i - p
    return str(p)

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))