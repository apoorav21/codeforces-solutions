def x():
    n, k = map(int, input().split())
    a = [*map(int, input().split())]
    if k == 1:
        return str(max(a))
    c = [0] * k
    p = 1
    for i in range(n):
        if c[p] < a[i]:
            c[p] = a[i]
        p += 1
        if p == k:
            p = 0
    return str(sum(c))

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))