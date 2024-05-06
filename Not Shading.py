for _ in range(int(input())):
    n, m, r, c = map(int, input().split())
    a = []
    x = 0
    for i in range(n):
        a.append(input())
    if a[r-1][c-1] == "B":
        print(0)
        continue
    if "B" in a[r-1]:
        print(1)
        continue
    for i in a:
        if i[c-1] == "B":
            x = 1
            break
    if x == 1:
        print(1)
    else:
        for i in a:
            if "B" in i:
                print(2)
                break
        else:
            print(-1)