for _ in range(int(input())):
    n, m = map(int, input().split())
    s = input()
    a = input()
    x = (n+m)
    s = s*x
    if a in s:
        count = 0
        x = s.index(a) + m
        while n < x:
            n = 2*n
            count += 1
        print(count)
    else:
        print(-1)