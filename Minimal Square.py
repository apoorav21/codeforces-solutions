for _ in range(int(input())):
    n = list(map(int, input().split()))
    if max(n) >= 2*min(n):
        print(max(n)**2)
    elif max(n) < 2*min(n):
        print((2*min(n)) ** 2)
    elif max(n) == min(n):
        print(max(n)**2)