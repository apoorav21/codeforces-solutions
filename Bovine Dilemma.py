def x():
    n = int(input())
    a = list(map(int, input().split()))
    s = set()
    for i in range(n):
        for j in range(i+1, n):
            s.add(a[j]-a[i])
    return str(len(s))


t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))