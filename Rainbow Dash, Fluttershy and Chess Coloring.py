def x():
    n = int(input())
    return str(n//2 + 1)

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))