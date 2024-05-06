for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    req = sum(a)//n
    x = 0
    for i in a:
        x += i-req
        if x<0:
            print("NO")
            break
    else:
        print("YES")