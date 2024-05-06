for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    count = 0
    for i in range(n-1):
        x = min(a[i],a[i+1])
        y = max(a[i],a[i+1])
        while y > 2*x :
            x = x*2
            count +=1
    print(count)