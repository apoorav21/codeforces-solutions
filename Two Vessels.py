for _ in range(int(input())):
    a, b, c = map(int, input().split())
    temp = max(a,b)
    b = min(a,b)
    a = temp
    count = 0
    while a>b:
        a = a-c
        b = b+c
        count += 1
    print(count)