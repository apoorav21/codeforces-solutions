for _ in range(int(input())):
    n = int(input())
    a = ""
    if n > 28:
        a += "z"
        n -= 26
        if n > 26:
            a = "z" + a
            n -= 26
            a = chr(n+96) + a
            print(a)
        else:
            n -= 1
            a = chr(n+96) + a
            a = "a" + a
            print(a)
    else:
        print("a",end="")
        n-= 1
        print("a",end="")
        n-= 1
        print(chr(n+96))
        