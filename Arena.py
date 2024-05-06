for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    print(n - a.count(min(a)))