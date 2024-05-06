for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    a = sorted(a,key=lambda x: x%2)
    print(*a)