for _ in range(int(input())):
    n, x = map(int, input().split())
    a = [*map(int, input().split())]
    a = sorted(a)
    for i,j in zip(a[n-1::-1],a[-1::-1]):
        if (j-i) < x:
            print("NO")
            break
    else:
        print("YES")