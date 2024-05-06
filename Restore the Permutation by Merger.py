for _ in range(int(input())):
    n = int(input())
    s = list(input().split())
    a = []
    for i in s:
        if i not in a:
            a.append(i)
    print(*a)