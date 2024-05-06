for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    count = 0
    for i,j in zip(a,a[1:]):   #here zip returns every pair of (a[i] a[i+1])
        if i > j:
            count = max(count, i)
    print(count)