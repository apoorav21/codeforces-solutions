for _ in range(int(input())):
    n, m = map(int, input().split())
    s = input()
    if m > 0:
        p = max(0,m - s.count("U"))
    else:
        p = min(0,m + s.count("D"))
    if n > 0:
        q = max(0, n - s.count("R"))
    else:
        q = min(0, n + s.count("L"))
    if m == 0:
        p = 0
    if n == 0:
        q = 0
    if p == 0 and q == 0:
        print("YES")
    else:
        print("NO")