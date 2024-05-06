for _ in range(int(input())):
    n = int(input())
    s = input()
    x = y = z =0
    for i in s:
        if i == 'U':
            y += 1
        if i == 'D':
            y -= 1
        if i == 'L':
            x -= 1
        if i == 'R':
            x += 1
        if x==1 and y==1:
            print("YES")
            z = 1
            break
    if z == 0:
        print("NO")