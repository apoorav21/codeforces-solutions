for _ in range(int(input())):
    n, d = map(int, input().split())
    a = [*map(int, input().split())]
    if max(a) <= d:
        print("YES")
        continue
    a.sort()
    if a[0]+a[1] > d:
        print("NO")
    else:
        print("YES")