for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [*map(int, input().split())]
    while k>0:
        for i in range(1,n):
            if a[i] != 0:
                a[i-1] += 1
                a[i] -= 1
                break
        k -= 1
    print(a[0])