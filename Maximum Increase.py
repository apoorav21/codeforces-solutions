n = int(input())
s = [*map(int, input().split())]
count = 0
res = 0
a = 0
for i in s:
    if i > a:
        count += 1
        res = max(res ,count)
    else:
        count = 1
    a = i
print(res)