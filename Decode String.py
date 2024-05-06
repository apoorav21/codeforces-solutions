for _ in range(int(input())):
    n = int(input())
    s = input()
    temp = ""
    s = s + "  "
    skiploop = 0
    for x in range(n):
        if skiploop:
            skiploop -= 1
        else:
            if s[x + 2] == "0" and s[x + 3] == "0":
                temp += chr(96 + int(s[x]))
            elif s[x + 2] == "0":
                temp += chr(96 + int(s[x : x + 2]))
                skiploop = 2
            else:
                temp += chr(96 + int(s[x]))
    print(temp)