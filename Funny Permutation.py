for _ in range(int(input())):
    n = int(input())
    if n == 3:
        print(-1)
    else:
        a = list(range(1,n-1))
        print(n,n-1,*a)