import math
a = [*map(int, input().split())]
i = 0
n = a[-1]
a.pop(-1)
while n >= 0:
    n -= math.gcd(a[i], n)
    i = 1 - i
print(i)