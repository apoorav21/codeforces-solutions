for _ in range(int(input())):
    n = int(input())
    s = [*map(int, input().split())]
    s.sort()
    a = s[-1] - s[0]
    for i in range(1,n):
        if s[i] - s[i-1] < a:
            a = s[i] - s[i-1]
    print(a)