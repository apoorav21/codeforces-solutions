def x():
    n, m = map(int, input().split())
    r = m * (n * (n + 1) + m - 1)
    r //= 2
    return str(r) 

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))