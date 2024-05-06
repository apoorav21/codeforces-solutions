def x():
    n = int(input())
    s =[]
    for i in range(n):
        s.append([*map(int, input().split())])
    w = s[0][0]
    e = s[0][-1]
    for i in s[1:]:
        if w <= i[0]:
            if e <= i[-1]:
                return "-1"
    return str(w)

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))