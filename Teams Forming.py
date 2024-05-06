n = int(input())
a = sorted([*map(int, input().split())])
count = 0
for i,j in zip(a[::2],a[1::2]):
    count += j-i
print(count)