n, k = map(int, input().split())
a = [*map(int, input().split())]
r = 0
for i in a:
    if i <= k:
        r += 1
    else:
        break
for i in reversed(a[r:]):
    if i <= k:
        r += 1
    else:
        break
print(r)