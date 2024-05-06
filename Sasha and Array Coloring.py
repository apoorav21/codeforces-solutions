for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    a.sort()
    res = 0
    for i in range(n // 2):
        res += a[-1 - x] - a[i]
    print(res)
