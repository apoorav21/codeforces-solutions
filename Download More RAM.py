for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    for i in range(n):
        for j in range(len(a)):
            if a[j] <= k:
                k += b[j]
                a.pop(j)
                b.pop(j)
                break
        else:
            break
    print(k)