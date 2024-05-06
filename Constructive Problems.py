def x():
    n, m = map(int, input().split())
    return str(max(n,m))

t = int(input())
a =[]
for _ in range(t):
    a.append(x())
print("\n".join(a))