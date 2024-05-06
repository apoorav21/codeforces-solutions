for _ in range(int(input())):
    n, k = map(int, input().split())
    if k > 0:
        for i in range(1,k+1):
            print(i,end=" ")
        for i in range(n,k,-1):
            print(i,end=" ")
        print()
    else:
        for i in range(n,0,-1):
            print(i,end=" ")
        print()