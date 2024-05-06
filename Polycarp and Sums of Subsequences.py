for _ in range(int(input())):
    n = list(map(int,input().split()))
    res = [n[0],n[1]]
    if n[2] != sum(res):
        res.append(n[2])
        print(*res)
    else:
        res.append(n[3])
        print(*res)