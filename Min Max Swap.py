for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    x = b.index(max(b))
    while a[x] < b[x]: 
        b[x] , a[x] = a[x] ,b[x]
        x = b.index(max(b))
    print(max(a)*max(b))