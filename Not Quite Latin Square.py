for _ in range(int(input())):
    for __ in range(3):
        s = input()
        a = ["A","B","C"]
        for i in s:
            try:
                a.remove(i)
            except:
                pass
        print(*a)