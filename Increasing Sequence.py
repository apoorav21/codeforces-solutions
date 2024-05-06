for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    c = 0
    for i in a:
        c += 1
        if c == i:
            c += 1
    print(c)