for _ in range(int(input())):
    n = int(input())
    s = [*map(int, input().split())]
    print(n-s.count(min(s)))