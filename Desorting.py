for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    x = float("inf")
    for i in range(n-1):
        x = min(x, a[i+1] - a[i])
    print(max(0, (x+2)//2))