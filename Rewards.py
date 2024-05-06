a = [*map(int, input().split())]
b = [*map(int, input().split())]
n = int(input())
x = 0
if sum(a) > 0:
    x += max(1,-(sum(a)//-5))
if sum(b) > 0:
    x+= max(1,-(sum(b)//-10))
if x <= n:
    print("YES")
else:
    print("NO")