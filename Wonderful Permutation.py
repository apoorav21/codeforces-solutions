for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [*map(int, input().split())]
    b = sorted(a)
    c = 0
    for i in range(k):
        if a[i] not in b[:k]:
            c += 1
    if k == n:
        print(0)
    else:
        print(c)