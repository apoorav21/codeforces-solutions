def x():
    n, m = map(int, input().split())
    x = []
    y = []
    for i in range(m):
        a,b = map(int, input().split())
        x.append(a)
        y.append(b)
    if len(x) < n or len(x) < n:
        return "YES"
    return "NO"


t = int(input())
a = []
for i in range(t):
    a.append(x())
print("\n".join(a))