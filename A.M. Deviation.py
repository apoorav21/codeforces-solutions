def x():
    s = [*map(int, input().split())]
    s.sort()
    m = abs(s[0]+s[2] - 2*s[1])
    if m%3 != 0:
        return "1"
    return "0"

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))