a = list(map(int, input().split()))
b= a.copy()
b.remove(max(b))
b.remove(min(b))

mid = int(b[0])

res = abs(a[0]-mid) + abs(a[1]-mid) + abs(a[2]-mid)
print(res)
