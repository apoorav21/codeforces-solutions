for _ in range(int(input())):
    a, b, c, n = map(int, input().split())
    x = max(a,b,c)
    if (n-((x-a)+(x-b)+(x-c)))%3 == 0 and (n-((x-a)+(x-b)+(x-c))) >= 0:
        print("YES")
    else:
        print("NO")