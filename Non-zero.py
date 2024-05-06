def x():
    n = int(input())
    a = [*map(int, input().split())]
    r = a.count(0)
    s = sum(a) + r
    if s == 0:
        r += 1
    return str(r)

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))