def x():
    n, s = map(int, input().split())
    a = [*map(int, input().split())]
    b = [int(i) for i in range(1,max(a)) if i not in a]
    r = sum(b)
    m = max(a)+1
    if s > r:
        while s > 0:
            s -= m
            m += 1
        if s < 0:
            return "NO"
        if s == 0:
            return "YES"
    return "NO"


t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))