for x in range(int(input())):
    n = int(input())
    s = (*map(int, input().split()),)
    m = 0
    for x, y in zip(s, s[1:]):
        temp = x * y
        if temp > m:
            m = temp
    print(m)