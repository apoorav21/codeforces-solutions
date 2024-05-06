def x():
    n = int(input())
    s = "1"
    for i in range(n,1,-1):
        s += str(i)
    return s

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))