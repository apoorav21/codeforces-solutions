for _ in range(int(input())):
    n, s, r = map(int, input().split())
    print(s-r,end=" ")
    for i in range(n-1):
        print((r+i)//(n-1),end=" ")
    print()