for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    count = 0
    x = min(a)
    y = min(b)
    for i in range(n):
        count += max(a[i]-x, b[i]- y)
    print(count)