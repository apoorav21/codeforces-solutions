n = int(input())
a = [*map(int, input().split())]
m = int(input())
s = []
for i in range(m):
    s.append([*map(int, input().split())])
r = []
for i in s:
    x = i[0]-1
    y = i[-1]
    try:
        a[x+1] += a[x] - y
    except:
        pass 
    try:
        a[x-1] += a[x] - 1 - y
    except:
        pass 
    a[x] = 0
print("\n".join(str(i) for i in a))