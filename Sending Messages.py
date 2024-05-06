for _ in range(int(input())):
    n, f, a, b = map(int, input().split())
    m = input()
    for i in range(n-1):
        if (int(m[n+1])-int(m[n])) < 2*b:
            f -= a
        else:
            f -= (2*b)+a

    if f > 0:
        print("YES")
    else:
        print("NO")