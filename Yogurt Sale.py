def x():
    n, a, b = map(int, input().split())
    if b < 2*a:
        return str((n//2)*b + (n%2)*a)
    return str(n*a)

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))