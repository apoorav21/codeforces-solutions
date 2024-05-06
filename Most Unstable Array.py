for _ in range(int(input())):
    n, m = map(int, input().split())
    if n >2:
        print(2*m)
    elif n == 2:
        print(m)
    else:
        print(0)
