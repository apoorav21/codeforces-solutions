x = []
y = []
t = int(input())
for _ in range(t):
    s = [*map(int, input().split())]
    x.append(s[0])
    y.append(s[-1])
r = 0
r += min(x.count(0),x.count(1))
r += min(y.count(0),y.count(1))
print(r)