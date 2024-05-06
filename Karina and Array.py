for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    c, b = [], []
    x = y = float("-inf")
    for i in a:
        if i < 0:
            c.append(i)
        else:
            b.append(i)
    if len(c) >= 2:
        x = min(c)
        c.remove(x)
        x *= min(c)
    if len(b) >= 2:
        y = max(b)
        b.remove(y)
        y *= max(b)
    if x == y == float("-inf"):
        print(a[0]*a[1])
    else:
        print(max(x,y))