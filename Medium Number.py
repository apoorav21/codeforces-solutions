for i in range(int(input())):
    s = list(map(int, input().split()))
    s.remove(min(s))
    s.remove(max(s))
    print(str(s[0]))