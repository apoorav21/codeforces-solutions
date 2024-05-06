def x():
    n, m = map(int, input().split())
    a = [*map(int, input().split())]
    r = max(a)
    b = max(a)
    if r > m:
        return "1"
    a.remove(r)
    r += max(a)
    if m%r != 0:
        if m%r -b > 0:
            return str((m//r)*2 + 2)
        else:    
            return str((m//r)*2 + 1)
    return str((m//r)*2)

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))