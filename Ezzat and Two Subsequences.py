for _ in range(int(input())):
    n = int(input())
    s = [*map(int, input().split())]
    a = max(s)
    s.remove(a)
    print(float((sum(s)/(n-1)))+a)