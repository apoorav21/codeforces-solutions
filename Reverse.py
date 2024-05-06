def x():
    n = int(input())
    s = [*map(int, input().split())]
    t = n
    for i in range(n):
        if s[i] != i+1:
            t = s.index(i+1)
            break
    r = list(s[:i] + s[i: t+1][::-1] + s[t+1 :])
    return " ".join(str(i) for i in r)

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))