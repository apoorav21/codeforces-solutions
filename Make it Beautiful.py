for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    if len(set(a)) > 1:
        a = sorted(a)
        print("YES")
        print(a[-1],*a[:-1])
    else:
        print("NO")