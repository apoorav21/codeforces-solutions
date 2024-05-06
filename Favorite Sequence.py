for _ in range(int(input())):
    n = int(input())
    s = [*map(int, input().split())]
    a = [0]*n
    while len(s) > 0:
        s.reverse()
        a.append(s.pop())
    print(*a)