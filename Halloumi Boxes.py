def x():
    n, k = map(int, input().split())
    a = [*map(int, input().split())]
    if a == sorted(a):
        return "YES"
    if k > 1:
        return "YES"
    return "NO"
t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))