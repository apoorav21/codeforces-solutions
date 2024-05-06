for _ in range(int(input())):
    n, k = map(int, input().split())
    if n%2 == 0:
        print("YES")
    elif k <= n and k % 2:
        print("YES")
    else:
        print("NO")