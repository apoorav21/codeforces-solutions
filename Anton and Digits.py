for _ in range(int(input())):
    two, three, five, six = map(int, input().split())
    a = min(two, five, six)    #no of 256
    b = min(three,(two - a))  #no if 32
    print((a*256)+(b*32))