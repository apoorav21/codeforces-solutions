for _ in range(int(input())):
    n, m = map(int, input().split())
    if (n+m)%2:
        print("Burenka")
    else:
        print("Tonya")