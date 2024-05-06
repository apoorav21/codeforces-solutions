for _ in range(int(input())):
    n = int(input())
    s = input()
    a = []
    i = 0
    while i < n-1:
        if s[i:i+2] not in a:
            a.append(s[i:i+2])
        i += 1
    print(len(a))