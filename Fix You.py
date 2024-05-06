for _ in range(int(input())):
    n, m = map(int, input().split())
    count = 0
    for i in range(n-1):
        s = input()
        if s[-1] != "D":
            count += 1
    s = input()
    count += s.count("D")
    print(count)