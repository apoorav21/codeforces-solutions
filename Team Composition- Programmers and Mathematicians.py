for _ in range(int(input())):
    a, b = map(int, input().split())
    m = min(a,b)
    print(min(m, (a+b)//4))