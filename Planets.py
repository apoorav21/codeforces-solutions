def x():
    n, c = map(int, input().split())
    a = [*map(int, input().split())]
    b = []
    s = 0
    for i in set(a):
        b.append(a.count(i))
    for i in b:
        if i  >= c:
            s += c
        else:
            s += i
    return str(s) 

t = int(input())
y = []
for _ in range(t):
    y.append(x())
print("\n".join(y))