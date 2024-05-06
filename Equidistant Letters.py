for _ in range(int(input())):
    s = input()
    a = set()
    for i in s:
        if s.count(i) == 2:
            a.add(i)
    for i in a:
        print(i,end="")
        print(i,end="")
    for i in s:
        if i not in a:
            print(i,end="")
    print()