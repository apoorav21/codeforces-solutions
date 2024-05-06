for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    for x in range(n):
        s = input().split()
        print(s)
        for i in s[1]:
            if i == 'D':
                if a[x] == 10:
                    a[x] = 0
                a[x] += 1
            else:
                if a[x] == -1:
                    a[x] = 9
                a[x] -= 1
        if a[x] == -1:
            a[x] = 9
        if a[x] == 10:
            a[x] = 0
    print(*a)    