def x():
    n, k = map(int, input().split())
    if k > n-2:
        return "1"
    return str(n)

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))