for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = sorted([*map(int, input().split())])
    b = sorted([*map(int, input().split())], reverse = True)
    i = j = l = 0
    while i<n and j<m:
        if a[i] + b[j] <= k:
            l += m-j 
            i += 1
        else:
            j += 1
    print(l)