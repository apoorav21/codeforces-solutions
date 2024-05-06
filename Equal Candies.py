for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    x = min(s)
    count = 0
    for i in s:
        count += i-x
    print(count)