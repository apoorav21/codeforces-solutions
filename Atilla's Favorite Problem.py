for _ in range(int(input())):
    n = int(input())
    s = input()
    a = []
    for i in s:
        a.append(i)
    a.sort()
    print(ord(a[-1]) - 96)