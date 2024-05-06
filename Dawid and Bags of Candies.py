a = [*map(int, input().split())]
a.sort()
if a[0] + a[-1] == a[1] + a[2] or a[-1] == sum(a[:-1]):
    print("YES")
else:
    print("NO")