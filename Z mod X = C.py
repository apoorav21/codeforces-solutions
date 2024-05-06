def x():
    a = [*map(int, input().split())]
    b = sorted(a)
    c = [0] * 3
    for i in range(3):
        c[a.index(b[i])] = str(sum(a[i:]))    
    return " ".join(c)

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))