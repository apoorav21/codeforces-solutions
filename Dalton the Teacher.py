for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    count = 0
    for i,j in enumerate(a):
        if i+1 == j:
            count += 1
    print(-(count//-2))