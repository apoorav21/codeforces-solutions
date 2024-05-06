for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a > abs(b-c) + c :
        print(2)
    elif abs(b-c) + c > a:
        print(1)
    else:
        print(3)