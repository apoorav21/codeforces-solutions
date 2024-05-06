for _ in range(int(input())):
    n = int(input())
    s = [*map(int, input().split())]
    a = s.count(2)
    c = j = 0
    for i in s[:-1]:
        if i == 2:
            c += 1
        if c == a-c:
            print(j+1)
            break
        j += 1
    else:
        print(-1)