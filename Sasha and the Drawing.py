t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print((k+1)//2 + (k == 4*n-2))