for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    a = sorted(a)
    b = []
    for i, j  in zip(a, a[n:]):
        b.append(i)
        b.append(j)
    print(*b)