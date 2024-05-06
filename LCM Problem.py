for _ in range(int(input())):
    a, b = map(int, input().split())
    if b < 2 * a:
        print(-1, -1)
    else:
        print(a, 2 * a)
