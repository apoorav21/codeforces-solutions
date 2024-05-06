for _ in range(int(input())):
    n = int(input())
    s = [*map(int, input().split())]
    if max(s)-1 in s or s.count(max(s)) > 1 or max(s) == 1:
        print("YES")
    else:
        print("NO")