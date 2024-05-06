for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    mx = a.index(max(a)) + 1
    mn = a.index(min(a)) + 1
    diff = abs(mn - mx)
    mn = [mn, n - mn + 1]
    mx = [mx, n - mx + 1]
    mx.sort()
    mn.sort()
    count = 0
    if mn[0] < mx[0]:
        count += mn[0]
        count += min(diff, mx[0])
    else:
        count += mx[0]
        count += min(diff, mn[0])
    print(count)