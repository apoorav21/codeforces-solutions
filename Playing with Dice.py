n, m = map(int, input().split())
a = (n + m)/2
b = int(a.is_integer())
a = int(a)
if n > m:
    print(6 - a, b, a - b)
elif n < m:
    print(a - b, b, 6 - a)
else:
    print(0,6,0)