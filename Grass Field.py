for _ in range(int(input())):
    i = sum([*map(int, input().split())])
    j = sum([*map(int, input().split())])
    print((i+j+2)//3)