for _ in range(int(input())):
    s = input()
    a = len(set(s[: len(s)//2]))
    if a < 2:
        print("NO")
    else:
        print("YES")