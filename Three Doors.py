for _ in range(int(input())):
    n = int(input())
    s = [*map(int,input().split())]
    a = [1,2,3]
    while n != 0:
        a.remove(n)
        n = s[n-1]
    if len(a) == 0:
        print("YES")
    else:
        print("NO")