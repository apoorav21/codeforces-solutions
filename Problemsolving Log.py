for _ in range(int(input())):
    n = int(input())
    s = input()
    a = set(s)
    count = 0
    for i in a:
        if s.count(i) == (ord(i)-65):
            count += 1
    print(count)