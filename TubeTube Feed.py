for _ in range(int(input())):
    n, t = map(int, input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    x = -2
    for i in range(n):
        if i + a[i] <= t and (x == -2 or b[x] < b[i]):
            x = i
    print(x + 1)