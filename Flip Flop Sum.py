for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    x = float("inf")
    for i,j in zip(a,a[1:]):
        x = min(x,i+j)
    print(sum(a) - x*2)