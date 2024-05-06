for _ in range(int(input())):
    n, m = map(int, input().split())
    if n == 1 or m == 1:
        print("YES")
    elif n*m <= 4:
        print("YES")
    else:
        print("NO")