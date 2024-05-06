for _ in range(int(input())):
    a, b, c = map(int, input().split())
    a -= 1
    b = b+c
    c = min(a,b)
    print(max(0,(c*2)+1))