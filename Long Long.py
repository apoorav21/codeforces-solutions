for _ in range(int(input())):
    n = int(input())
    s = [*map(int, input().split())]
    Sum = count = 0
    x = 1 
    for i in s:
        if i < 0:
            Sum -= i
            count += x
            x = 0
        elif i > 0:
            Sum += i
            x = 1
    print(Sum, count)