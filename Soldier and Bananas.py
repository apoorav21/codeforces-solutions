k, n, w = map(int, input().split())
x = 0
for i in range(1,w+1):
    x = x + (k*i)


y = (x - n)

print(max(0,y))