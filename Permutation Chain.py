def x():
    n = int(input())
    s = " ".join(map(str, range(2, n + 1)))
    c = [str(n), "1 " + s]
    p = 1
    ll = len(s)
    while p < ll:
        if s[p] == " ":
            p += 1
            c.append(s[:p] + "1 " + s[p:])
        p += 1
    c.append(s + " 1")
    return "\n".join(c)

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))