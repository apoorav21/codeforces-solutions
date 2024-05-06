for _ in range(int(input())):
    n = int(input())
    s = [*map(int, input().split())]
    f = [*map(int, input().split())]
    a = []
    a.append(f[0] - s[0])
    for i in range(1,n):
        if s[i] > f[i-1]:
            a.append(f[i]-s[i])
        else:
            a.append(f[i]-f[i-1])
    print(*a)