for _ in range(int(input())):
    n = int(input())
    s = input()
    a = ""
    for i in s:
        if not a:
            a = i
        elif a == i:
            print(a, end="")
            a = ""
    print()