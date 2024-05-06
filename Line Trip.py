def x():
    n, x = map(int, input().split())
    a = [0] + [*map(int, input().split())]
    a.append(x)
    m = 0
    for i,j in zip(a,a[1:]):
        m = max(m, j-i)
    return (max(m, 2*(x - a[-2])))
    
t = int(input())
b = []
for _ in range(t):
    b.append(x())
print("\n".join(str(i) for i in b))