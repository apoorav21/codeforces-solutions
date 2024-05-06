for _ in range(int(input())):
    n = int(input())
    s = input()
    if "ab" in s:
        a = s.index("ab") + 1
        print(a , a+1)
    elif "ba" in s:
        a = s.index("ba") + 1
        print(a , a+1)
    else:
        print(-1, -1)