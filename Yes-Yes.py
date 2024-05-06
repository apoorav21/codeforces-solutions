for _ in range(int(input())):
    s = input()
    if s[0] in "Yes":
        a = "Yes".index(s[0])
        b = len(s)//3
        c = "Yes" * (b +2)
        d = c[a : a+len(s)]
        print(["no", "yes"][d == s])
    else:
        print("no")