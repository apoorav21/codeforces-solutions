for _ in range(int(input())):
    a, b = map(int,input().split())
    if a == b:
        print(0)
    elif a>b:
        diff = a-b
        if diff%2 == 0:
            print(1)
        else:
            print(2)
    else:
        if (b-a)%2 == 0:
            print(2)
        else:
            print(1)