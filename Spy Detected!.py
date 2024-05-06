for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))

    a = set(s)

    if s.count(a[0]) > s.count(a[1]):
        print(s.index(a[1]) + 1)
    else:
        print(s.index(a[0]) + 1)
