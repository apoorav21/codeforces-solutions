def x():
    n = int(input())
    s = map(int, input().split())
    r = 0
    for i in s:
        r |= i
    return str(r)

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))