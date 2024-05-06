for _ in range(int(input())):
    n = [*(input())]
    if len(n) > 2:
        print(min(n))
    else:
        print(n[-1])