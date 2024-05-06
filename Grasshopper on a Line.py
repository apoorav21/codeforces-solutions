for _ in range(int(input())):
    x, k = map(int, input().split())
    if k > x:
        print(1)
        print(x)
    else:
        if x%k != 0:
            print(1)
            print(x)
        else:
            print(2)
            if x < 0:
                print(x+1, -1)
            else:
                print(x-1, 1)