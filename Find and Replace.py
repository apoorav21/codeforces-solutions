for _ in range(int(input())):
    n = int(input())
    s = input()
    print('NO'if set(s[::2])&set(s[1::2]) else'YES')