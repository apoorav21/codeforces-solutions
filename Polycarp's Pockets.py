n = int(input())
a = [*map(int, input().split())]
x = 0
for i in a:
    x = max(x, a.count(i))
print(x)