for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    a.sort()
    b.sort()
    j = -1
    for i in range(k):
        if a[i] <= b[j]:
            a[i] = b[j] 
        j += -1
    print(sum(a))
