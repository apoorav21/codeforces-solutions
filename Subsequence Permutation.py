for _ in range(int(input())):
    n = int(input())
    s = input()
    a = sorted(s)
    count = 0
    for i in range(n):
        if a[i] != s[i]:
            count += 1
    print(count)