for _ in range(int(input())):
    n, m = map(int, input().split())
    everyc = [""] * m
    for x in range(n):
        x = input()
        for i in range(m):
            everyc[i] += x[i]
    temp = 0
    key = "vika"
    for x in everyc:
        if key[temp] in x:
            if temp < 3:
                temp += 1
            elif temp == 3:
                print("yes")
                break
    else:
        print("no")