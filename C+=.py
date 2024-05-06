for _ in range(int(input())):
    a, b, c = map(int, input().split())
    count = 0
    while b <= c:
        a, b = max(a, b), a + b
        count += 1
    print(count)