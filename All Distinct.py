for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    x = set(a)
    count = (n - set(a))//2
    print(count)