for _ in range(int(input())):
    n = int(input())
    s = [*map(int, input().split())]
    a = s.count(1)
    print(n-a//2)