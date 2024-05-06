for _ in range(int(input())):
    n = int(input())
    s = [*map(int,input().split())]
    a = sum(s)%n
    if a != 0:
        print(-1)
    else:
        s.sort()
        for i in range(1,n+1):
            if s[-i] <= a:
                print(i)
                break