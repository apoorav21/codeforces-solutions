n = int(input())
x = 0
total = 0
for i in range(n):
    a , b = map(int, input().split())
    total += b - a
    x = max(x,total)

print(x)
