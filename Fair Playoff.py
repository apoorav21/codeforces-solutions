for _ in range(int(input())):
    s = [*map(int, input().split())]
    a = max(s[0],s[1])
    b = max(s[-1],s[-2])
    s.sort()
    if (a == s[-1] or a == s[-2]) and (b == s[-1] or b == s[-2]):
        print("YES")
    else:
        print("NO")