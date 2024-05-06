for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input())]
    if len(set(a)) > 1:
        x = a.count(max(a))
        c = []
        for i in range(x):
            c.append(max(a))
            a.pop(max(a))
        print(n-x,x)
        print(*a)
        print(c)
    else:
        print(-1)