for _ in range(int(input())):
    s = input()
    res = 0
    while len(s)>0:
        a = []
        count = 0
        for i in s:
            if i not in a:
                a.append(i)
            if len(a) == 3:
                break
        for i in s:
            if i in a:
                count += 1
            else:
                break
        s = s[count:]
        res += 1
    print(res)