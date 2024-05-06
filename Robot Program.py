def x():
    s = list(map(int, input().split()))
    s.append(abs(s[0] - s[1]))
    if s[2]:
        return str(sum(s) - 1)
    return str(sum(s))

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))