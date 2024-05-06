for _ in range(int(input())):
    a = list(map(int, input().split()))
    m = max(a)
    a.remove(m)
    if m == sum(a):
        print("YES")
    else:
        print("NO")