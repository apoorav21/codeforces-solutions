for _ in range(int(input())):
    res = prev = 0
    count = 1    
    for i in range(int(input())):
        a, b = map(int, input().split())
        if a <= 10:
            if b > prev:
                res = count
                prev = b
        count += 1
    print(res)
