for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    m = float("-inf")
    for i in a:
        m = max(m,a.count(i))
    print(m)