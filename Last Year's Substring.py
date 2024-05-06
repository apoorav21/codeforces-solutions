for _ in range(int(input())):
    n = int(input())
    s = input()
    res = "no"
    for i in range(5):
        if (s[:i] + s[n-(4-i):] == "2020"):
            res = "yes"
    print(res)