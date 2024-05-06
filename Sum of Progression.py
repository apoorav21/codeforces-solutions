for _ in range(int(input())):
    n, q = map(int, input().split())
    f = list(map(int,input().split()))
    
    for __ in range(q):
        s, d, k = map(int, input().split())
        j=1
        sum = 0

        for i in range(k):
            sum += (f[s-1])*j
            s += d
            j +=1

        print(sum)