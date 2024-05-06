for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        s = input().split()
        a.append(s)
    x = y = z = float("inf")
    for i in a:
        if i[1][0] == "1":
            x = min(x, int(i[0]))
        elif i[1][1] == "1":
            y = min(y, int(i[0]))
        if i[1] == "11":
            z = min(z, int(i[0]))
    if (x == float("inf") or y == float("inf")) and z == float("inf"):
        print(-1)
    else:
        print(min(x+y,z))