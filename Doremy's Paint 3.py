def x():
    n = int(input())
    a = [*map(int, input().split())]
    s = set(a)
    l = list(s)
    if len(s) == 1 or (len(s) == 2 and abs(a.count(l[0])- a.count(l[1])) < 2):
        return "YES"
    return "NO"

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))