for _ in range(int(input())):
    n = int(input())
    s = [*map(int, input().split())]
    count = 0
    res = 0
    for i in s:
        if i == 0:
            count += 1
            res = max(res,count)
        else:
            count = 0
    print(res)