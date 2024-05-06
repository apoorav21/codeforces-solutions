n, c = map(int, input().split())
a = [*map(int, input().split())]
r = 1
x = a[0]
for i in a[1:]:
    if i - x > c:
        r = 1
    else:
        r += 1
    x = i
print(r)