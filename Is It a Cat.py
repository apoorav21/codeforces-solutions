for _ in range(int(input())):
    input()
    s = input().lower()
    a = s[0]
    for i in s:
        if a[-1] != i:
            a += i
    if a == "meow":
        print("YES")
    else:
        print("NO")