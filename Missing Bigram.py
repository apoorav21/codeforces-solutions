def x():
    n = int(input())
    s = input().split()
    r = s[0]
    for i in range(1, n-2):
        if s[i][0] == s[i-1][-1]:
            r += s[i][1]
        else:
            r += s[i]
    if len(r) != n:
        r += "a"
    return r

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))