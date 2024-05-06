for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    x = 0
    for i in a:
        if i < 0:
            x += 1
    if x%2 or (0 in a) :
        print(0)
    else:
        print(1)
        print(1, 0)