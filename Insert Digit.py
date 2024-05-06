for _ in range(int(input())):
    n, k = input().split()
    s = input()
    for i in range(int(n)):
        if k > s[i]:
            print(s[:i] + k + s[i:])
            break
    else:
        print(s + k)