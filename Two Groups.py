for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    x = y = 0
    for i in a:
        if i > 0:
            x += i
        else:
            y += i
    print(abs(x-(-y)))