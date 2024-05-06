for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    x = a[0] - b[0]
    for i,j in zip(a,b):
        if i < j:
            print("NO")
            break
        x = max(x, i-j)
    else:    
        for i in range(n):
            a[i] = max(0,a[i]-x)
        if a == b:
            print("YES")
        else:
            print("NO")