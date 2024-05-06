for _ in range(int(input())):
    n, m, k = map(int,input().split())
    x = (m-1) + m*(n-1)
    if x == k:
        print("YES")
    else:
        print("NO") 