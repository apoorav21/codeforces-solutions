for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    for i in a:
        if i in b:
            print("YES")
            print(1, i)
            break
    else:
        print("NO")