input()
a = [*map(int, input().split())]
print(a.count(1))
b = []
for i,j in zip(a,a[1:]):
    if j == 1:
        b.append(i)
b.append(a[-1])
print(" ".join(str(i) for i in b))