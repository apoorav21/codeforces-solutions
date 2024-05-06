for _ in range(int(input())):
    s = input().split("0")
    s = sorted(s)
    a = 0
    for i in s[-1::-2]:
        a += len(i)
    print(a)