for _ in range(int(input())):
    n, k = map(int, input().split())
    if (n+1)//2 < k:
        print(-1)
    else:
        x = y = 0
        r = [n*['.'] for i in range(n)]
        for i in range(k):
            r[i*2][i*2] = "R"
        for i in r:
            print(''.join(str(j) for j in i))