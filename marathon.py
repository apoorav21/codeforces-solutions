for _ in range(int(input())):
    s = list(map(int, input().split()))
    count = 0
    for i in s[1:]:
        if i >= s[0]:
            count += 1
    print(count)