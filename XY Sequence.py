def x():
    n, b, x, y = map(int, input().split())
    c = k = 0
    for i in range(n):
        if k + x <= b:
            k += x
            c += k
        else:
            k -= y
            c += k
    return str(c)


t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(str(i) for i in a))