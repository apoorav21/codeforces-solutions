def x():
    n = int(input())
    return str(n**2 + n*2 + 2)

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))