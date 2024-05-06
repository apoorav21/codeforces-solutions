for _ in range(int(input())):
    n = int(input())
    if n%2050 > 0:
        print(-1)
    else:
        if n//2050 >= 10:
            s = [*str(n//2050)]
            print(sum(int(i) for i in s))
        else:
            print(n//2050)