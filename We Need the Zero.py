def x():
    n = int(input())
    a = [*map(int, input().split())]
    r = 0
    for i in a:
        r ^= i
    if n%2 == 0 and r != 0:
        return "-1"
    return str(r)

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))