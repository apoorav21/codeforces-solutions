def x():
    n = int(input())
    a = [*map(int, input().split())]
    if n < 3:
        if a == sorted(a):
            return "NO"
        return "YES"
    x = a[0]
    for i in range(n):
        if a[i] < x:
            return "YES"
        x = a[i]
    return "NO"

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))