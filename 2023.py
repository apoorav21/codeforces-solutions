for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [*map(int, input().split())]
    p = 1
    for i in a:
        p *= i
    if 2023%p != 0:
        print("NO")
    else:
        print("YES")
        print(2023//p, "1 "*(k-1))