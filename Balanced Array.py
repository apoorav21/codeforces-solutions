for _ in range(int(input())):
    n = int(input())
    if n//2 %2 != 0:
        print("NO")
    else:
        a = range(2,n+1,2)
        b = range(1,n-1,2)
        c = sum(a) - sum(b)
        a = list(map(str, a)) + list(map(str, b)) + [str(c)]

        print("YES")
        print(' '.join(a))

