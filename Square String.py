for _ in range(int(input())):
    s = input()
    b = []
    n = len(s)
    if n%2:
        print("NO")
    else:
        if s[:n//2] == s[n//2:]:
            print("YES")
        else:
            print("NO")
