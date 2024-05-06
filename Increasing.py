for _ in range(int(input())):
    n = int(input())
    s = [*map(int, input().split())]
    x = 0
    for i in s:
        if s.count(i) > 1:
            print("NO")
            x = 1
            break
    if x == 0:
        print("YES")