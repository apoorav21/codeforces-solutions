for _ in range(int(input())):
    a, b, c = map(int, input().split())
    mx = a
    count = 1
    for i in (b,c):
        if mx == i:
            count += 1
        elif i > mx:
            mx = i
            count = 1
    if count > 1:
        res = (mx + 1 - x for x in (a, b, c))
        print(" ".join(map(str, res)))
    else:
        z = []
        for i in (a,b,c):
            if i == mx:
                z.append(0)
            else:
                z.append(mx + 1 - i)
        print(*z)
