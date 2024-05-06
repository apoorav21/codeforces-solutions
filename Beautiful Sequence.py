def x():
    n = int(input())
    a = [*map(int, input().split())]
    for i, j in enumerate(a, start=1):
        if i >= j:
            return "YES"
    return "NO"

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))