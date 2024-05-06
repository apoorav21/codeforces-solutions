def x():
    n = int(input())
    a = [*map(int, input().split())]
    m = int(input())
    b = [*map(int, input().split())]
    m1 = max(a)
    m2 = max(b)
    if m1 > m2:
        return "Alice\n" + "Alice"
    elif m1 < m2:
        return "Bob\n" + "Bob"
    else:
        return "Alice\n" + "Bob"

t = int(input())
a =[]
for _ in range(t):
    a.append(x())
print("\n".join(a))