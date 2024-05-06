for _ in range(int(input())):
    n, m = map(int, input().split())
    t = min(n,m)
    m = max(m,n)
    n = t
    count = 0
    if m%2 != 0:
        count += ((m-1)//2)*n + -(n//-2)
    else:
        count += ((m)//2)*n
    print(count)