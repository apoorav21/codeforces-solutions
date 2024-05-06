for j in range(int(input())):
    w, h, n = map(int, input().split())
    count = 1
    while count < n:
        if w % 2 == 0:
            count *= 2
            w //= 2
        elif h % 2 == 0:
            count *= 2
            h //= 2
        else:
            print("NO")
            break
    else:
        print("YES")