for _ in range(int(input())):
    n, m = map(int, input().split())
    if n == m == 0:
        print(0)
    elif n == 0 or m == 0:
        print(1)
    elif (((n**2) + (m**2))**0.5)%1 == 0:
        print(1)
    else:
        print(2)