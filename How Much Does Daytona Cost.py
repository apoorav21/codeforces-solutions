for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [*map(int, input().split())]
    if k not in a:
        print("NO")
    else:   
        print("YES")                   