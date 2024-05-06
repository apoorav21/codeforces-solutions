for _ in range(int(input())):
    n, m = map(int, input().split())
    s = [*map(int, input().split())]
    res = m - sum(s)
    if res > 0:
        res = 0
    print(abs(res))