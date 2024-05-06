n, m = map(int, input().split())
a = b = count = 0
while a**2 <= n:
    a += 1
while b**2 <= m:
    b += 1
for i in range(a):
    for j in range(b):
        if i**2 + j == n and j**2 + i == m:
            count += 1

print(count)