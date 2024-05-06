for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    total = sum(a)
    if total < n :
        print(1)
    else:
        print(abs(n - total))