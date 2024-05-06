a = sorted(list(map(int, input().split())))
if a[0] + a[1] > a[-1]:
    print(0)
else:
    print(a[-1] - (a[0] + a[1]) + 1)