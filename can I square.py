for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    s = sum(a)
    x = s**0.5
    if int(x)**2 == s:
        print("YES")
    else:
        print("NO")