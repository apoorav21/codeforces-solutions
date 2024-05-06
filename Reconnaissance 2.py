n = int(input())
s = [*map(int, input().split())]
d = abs(s[0] - s[-1])
res = (1,n)
for i in range(n-1):
    if d > abs(s[i] - s[i+1]):
        d = abs(s[i] - s[i+1])
        res = (i+1, i+2)
print(*res)