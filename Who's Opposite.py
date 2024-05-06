for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if abs(a - b)*2  > max(a,b,c):
        if c + abs(a-b) > abs(a - b)*2:
            print(abs(c-(abs(a-b))))
        else:
            print(c + abs(a-b))
    else:
       print(-1)
