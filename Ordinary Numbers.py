for _ in range(int(input())):
    n = input()
    x = n[0] * len(n)
    if n >= x:
        print(9*(len(n) - 1) + int(n[0]))
    else:
        print(9*(len(n) - 1) + int(n[0])-1) 