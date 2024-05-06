def x():
    n, k = map(int, input().split())
    a = [*map(int, input().split())]
    c = 0
    if k == 1:
        return str((n-1)//2)
    for i in range(1, n-1):
        if a[i] > (a[i-1] + a[i+1]):
            c += 1
    return str(c)

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))