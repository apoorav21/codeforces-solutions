def x():
    n, m = map(int, input().split())
    r = sum([*map(int, input().split())])
    if r == m:
        return "YES"
    return "NO"

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))